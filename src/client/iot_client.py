import os
import argparse
import flwr as fl
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
import numpy as np
import sys

# Add parent dir to path so we can import from src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.ids_model import get_model

# Constants
# Reduced batch size significantly for MPS memory/scheduling considerations
BATCH_SIZE = 64

def load_local_data(client_id, processed_dir="data/processed"):
    """Load the partitioned data for this specific client."""
    client_dir = os.path.join(processed_dir, f"client_{client_id}")
    
    print(f"Loading data from {client_dir}...")
    X_train = torch.load(os.path.join(client_dir, 'X_train.pt'))
    y_train = torch.load(os.path.join(client_dir, 'y_train.pt'))
    
    # Create DataLoader
    # Limit data per client to 10000 sequences to ensure the simulation iteration finishes quickly
    # (Otherwise 167k sequences * 5 clients takes too long for a single demo round)
    subset_size = min(len(X_train), 10000)
    dataset = TensorDataset(X_train[:subset_size], y_train[:subset_size])
    dataloader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True)
    
    return dataloader, subset_size

def train(model, trainloader, epochs, device):
    """Train the network on the training set."""
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    
    model.train()
    for epoch in range(epochs):
        running_loss = 0.0
        correct = 0
        total = 0
        for data, target in trainloader:
            data, target = data.to(device), target.to(device)
            optimizer.zero_grad()
            outputs = model(data)
            loss = criterion(outputs, target)
            loss.backward()
            optimizer.step()
            
            running_loss += loss.item() * data.size(0)
            _, predicted = torch.max(outputs.data, 1)
            total += target.size(0)
            correct += (predicted == target).sum().item()
            
        epoch_loss = running_loss / len(trainloader.dataset)
        epoch_acc = correct / total
        print(f"Epoch {epoch+1}/{epochs} | Loss: {epoch_loss:.4f} | Accuracy: {epoch_acc:.4f}")

# Define the Flower Client definition
class IdsClient(fl.client.NumPyClient):
    def __init__(self, model, trainloader, num_examples, device):
        self.model = model
        self.trainloader = trainloader
        self.num_examples = num_examples
        self.device = device

    def get_parameters(self, config):
        """Get model weights as a list of NumPy ndarrays."""
        return [val.cpu().numpy() for _, val in self.model.state_dict().items()]

    def set_parameters(self, parameters):
        """Set model weights from a list of NumPy ndarrays."""
        params_dict = zip(self.model.state_dict().keys(), parameters)
        state_dict = {k: torch.tensor(v) for k, v in params_dict}
        self.model.load_state_dict(state_dict, strict=True)

    def fit(self, parameters, config):
        """Train the model on the local data and return the updated weights."""
        print(f"--- Client starting training round ---")
        self.set_parameters(parameters)
        
        # Train on local data
        epochs = config.get("epochs", 1)
        train(self.model, self.trainloader, epochs, self.device)
        
        # Return updated parameters and number of examples used for weighting
        return self.get_parameters(config=None), self.num_examples, {}

    def evaluate(self, parameters, config):
        # We perform evaluation centrally on the server, so clients don't evaluate locally here.
        return 0.0, self.num_examples, {"accuracy": 0.0}

def main():
    parser = argparse.ArgumentParser("IoT FL Client")
    parser.add_argument("--client-id", type=int, required=True, help="Client ID for loading specific data shard (1, 2, 3...)")
    parser.add_argument("--model-type", type=str, default="lstm", choices=["lstm", "gru"], help="Model type to use")
    parser.add_argument("--server-addr", type=str, default="127.0.0.1:8080", help="Address of the FL server")
    args = parser.parse_args()

    # Determine device
    # On Mac M1/M2/M3/M4, MPS can sometimes hang with large batches/many threads in multiprocessing.
    device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
    
    # Optional: fallback to CPU if explicitly requested or if MPS has issues
    if os.environ.get("FORCE_CPU") == "1":
         device = torch.device("cpu")
         
    print(f"Client {args.client_id} using device: {device}")

    # Load data for this client
    trainloader, num_examples = load_local_data(args.client_id)

    # Initialize model
    model = get_model(model_type=args.model_type, input_size=46, hidden_size=64, num_classes=8, num_layers=1).to(device)

    # Start Flower client
    client = IdsClient(model, trainloader, num_examples, device)
    
    print(f"Connecting to FL server at {args.server_addr}...")
    fl.client.start_numpy_client(
        server_address=args.server_addr,
        client=client,
    )

if __name__ == "__main__":
    main()
