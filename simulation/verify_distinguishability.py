import torch
from torch.utils.data import DataLoader, TensorDataset
import numpy as np
import time
import os
import sys

# Add parent dir to path so we can import from src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.models.ids_model import get_model

def test_data_distinguishability(processed_dir="data/processed", model_type="lstm", epochs=3):
    """
    Train a standard (non-federated) local model on a slice of data to definitively prove
    if the LSTM can distinguish between Benign and Attack sequences.
    """
    print(f"Loading data from {processed_dir}...")
    
    # Load labels to check data distribution
    y_train = torch.load(os.path.join(processed_dir, 'y_train.pt'))
    classes = np.load(os.path.join(processed_dir, 'classes.npy'), allow_pickle=True)
    
    benign_idx = np.where(classes == 'Benign')[0]
    if len(benign_idx) == 0:
        print("Warning: 'Benign' class not found in the encoded classes!")
    else:
        benign_val = benign_idx[0]
        # Calculate distribution
        total = len(y_train)
        benign_count = torch.sum(y_train == benign_val).item()
        attack_count = total - benign_count
        print(f"\n--- Data Distribution Context ---")
        print(f"Total training sequences: {total}")
        print(f"Benign  ('Normal') sequences: {benign_count} ({benign_count/total*100:.2f}%)")
        print(f"Attack             sequences: {attack_count} ({attack_count/total*100:.2f}%)")
        print("-" * 33 + "\n")
        
    # For Binary Classification Check (Attack=1, Benign=0)
    y_train_binary = (y_train != benign_val).long()
    
    print("Loading features...")
    X_train = torch.load(os.path.join(processed_dir, 'X_train.pt'))
    
    # We'll train on 50,000 samples locally to prove it works quickly
    SubsetSize = min(50000, len(X_train))
    dataset = TensorDataset(X_train[:SubsetSize], y_train_binary[:SubsetSize])
    trainloader = DataLoader(dataset, batch_size=256, shuffle=True)
    
    device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
    print(f"Training Baseline Local {model_type.upper()} BINARY model on {device}...")
    
    # Calculate class weights for the loss function to handle the 82/18 imbalance
    num_attacks = torch.sum(y_train_binary[:SubsetSize] == 1).item()
    num_benign = SubsetSize - num_attacks
    weight_benign = SubsetSize / (2.0 * max(1, num_benign))
    weight_attack = SubsetSize / (2.0 * max(1, num_attacks))
    class_weights = torch.tensor([weight_benign, weight_attack], dtype=torch.float32).to(device)
    print(f"Applying Class Weights -> Benign: {weight_benign:.2f}, Attack: {weight_attack:.2f}")
    
    # Num classes = 2 (Benign vs Attack)
    model = get_model(model_type=model_type, input_size=46, hidden_size=256, num_classes=2, num_layers=2).to(device)
    criterion = torch.nn.CrossEntropyLoss(weight=class_weights)
    optimizer = torch.optim.Adam(model.parameters(), lr=0.005)
    scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer, 'min', patience=2, factor=0.5)
    
    for epoch in range(epochs):
        model.train()
        running_loss = 0.0
        correct = 0
        total_preds = 0
        
        start_t = time.time()
        for data, target in trainloader:
            data, target = data.to(device), target.to(device)
            optimizer.zero_grad()
            outputs = model(data)
            loss = criterion(outputs, target)
            loss.backward()
            optimizer.step()
            
            running_loss += loss.item() * data.size(0)
            _, predicted = torch.max(outputs.data, 1)
            total_preds += target.size(0)
            correct += (predicted == target).sum().item()
            
        epoch_loss = running_loss / SubsetSize
        epoch_acc = correct / total_preds
        
        scheduler.step(epoch_loss)
        lr = optimizer.param_groups[0]['lr']
        print(f"Epoch {epoch+1}/{epochs} | Loss: {epoch_loss:.4f} | Accuracy: {epoch_acc*100:.2f}% | LR: {lr:.5f} | Time: {time.time()-start_t:.1f}s")

    print("\nTraining complete. Evaluating on separate Test Slice...")
    X_test = torch.load(os.path.join(processed_dir, 'X_test.pt'))
    y_test = torch.load(os.path.join(processed_dir, 'y_test.pt'))
    y_test_binary = (y_test != benign_val).long()
    
    test_subset = min(10000, len(X_test))
    test_data = TensorDataset(X_test[:test_subset], y_test_binary[:test_subset])
    testloader = DataLoader(test_data, batch_size=256, shuffle=False)
    
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for data, target in testloader:
            data, target = data.to(device), target.to(device)
            outputs = model(data)
            _, predicted = torch.max(outputs.data, 1)
            total += target.size(0)
            correct += (predicted == target).sum().item()
            
    test_acc = correct / total
    print(f"Final Test Accuracy: {test_acc*100:.2f}%\n")
    print("If Accuracy is high (>90%), then YES, the LSTM can easily distinguish.")
    
    # Save the definitively trained model for the simulator to use directly!
    os.makedirs("saved_models", exist_ok=True)
    save_path = f"saved_models/local_verified_{model_type}.pth"
    torch.save(model.state_dict(), save_path)
    print(f"Saved definitively trained baseline model to: {save_path}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-type", type=str, default="gru", choices=["lstm", "gru"])
    parser.add_argument("--epochs", type=int, default=15)
    args = parser.parse_args()
    
    test_data_distinguishability(model_type=args.model_type, epochs=args.epochs)
