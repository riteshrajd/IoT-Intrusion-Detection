import os
import argparse
import flwr as fl
import torch
from torch.utils.data import DataLoader, TensorDataset
from flwr.server.strategy import FedAvg
import sys
import numpy as np

# Add parent dir to path so we can import from src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.ids_model import get_model

# Constants
# Evaluation batch size
BATCH_SIZE = 256

def get_evaluate_fn(model_type, processed_dir="data/processed", device="cpu"):
    """Return an evaluation function for server-side evaluation."""
    
    print(f"Loading global test data from {processed_dir} for evaluation...")
    try:
        X_test = torch.load(os.path.join(processed_dir, 'X_test.pt'))
        y_test = torch.load(os.path.join(processed_dir, 'y_test.pt'))
    except FileNotFoundError:
        print("Error: Test tensors not found. Please run preprocess.py first.")
        # Return a dummy function that returns 0.0 if data isn't generated yet
        return lambda server_round, parameters, config: (0.0, {"accuracy": 0.0})

    # To avoid memory lockups on Mac M4 with 1M rows, evaluate only on a subset
    subset_size = min(len(X_test), 20000)
    dataset = TensorDataset(X_test[:subset_size], y_test[:subset_size])
    testloader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=False)
    
    # Initialize the model structure
    model = get_model(model_type=model_type, input_size=46, hidden_size=64, num_classes=8, num_layers=1).to(device)
    criterion = torch.nn.CrossEntropyLoss()

    # The `evaluate` function will be called by Flower after every round
    def evaluate(server_round, parameters, config):
        print(f"--- Server evaluating round {server_round} ---")
        
        # Load the newly aggregated weights
        params_dict = zip(model.state_dict().keys(), parameters)
        state_dict = {k: torch.tensor(v) for k, v in params_dict}
        model.load_state_dict(state_dict, strict=True)
        
        model.eval()
        loss = 0.0
        correct = 0
        total = 0
        
        with torch.no_grad():
            for data, target in testloader:
                data, target = data.to(device), target.to(device)
                outputs = model(data)
                loss += criterion(outputs, target).item() * data.size(0)
                
                _, predicted = torch.max(outputs.data, 1)
                total += target.size(0)
                correct += (predicted == target).sum().item()
                
        loss = loss / len(testloader.dataset)
        accuracy = correct / total
        
        print(f"Round {server_round} | Global Aggregated Loss: {loss:.4f} | Accuracy: {accuracy:.4f}")
        
        # Save the global model 
        os.makedirs("saved_models", exist_ok=True)
        save_path = f"saved_models/global_{model_type}_round_{server_round}.pth"
        torch.save(model.state_dict(), save_path)
        print(f"Saved global model to {save_path}")
        
        return loss, {"accuracy": accuracy}

    return evaluate

def main():
    parser = argparse.ArgumentParser("IoT FL Server")
    parser.add_argument("--rounds", type=int, default=3, help="Number of FL communication rounds")
    parser.add_argument("--min-clients", type=int, default=2, help="Minimum number of clients required to start")
    parser.add_argument("--model-type", type=str, default="lstm", choices=["lstm", "gru"], help="Model type to aggregate")
    parser.add_argument("--server-addr", type=str, default="0.0.0.0:8080", help="Address to bind the server to")
    args = parser.parse_args()

    # Determine device for evaluation
    device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
    
    if os.environ.get("FORCE_CPU") == "1":
         device = torch.device("cpu")
         
    print(f"Server evaluation using device: {device}")

    # Create strategy (Federated Averaging)
    strategy = FedAvg(
        fraction_fit=1.0,  # Sample 100% of available clients for training
        fraction_evaluate=1.0, # Sample 100% for evaluation (we'll do centralized instead)
        min_fit_clients=args.min_clients,
        min_evaluate_clients=args.min_clients,
        min_available_clients=args.min_clients,
        evaluate_fn=get_evaluate_fn(args.model_type, device=device),
        initial_parameters=None,
    )

    print(f"Starting FL server on {args.server_addr} for {args.rounds} rounds...")
    fl.server.start_server(
        server_address=args.server_addr,
        config=fl.server.ServerConfig(num_rounds=args.rounds),
        strategy=strategy,
    )

if __name__ == "__main__":
    main()
