import os
import torch
import numpy as np

def split_data_for_clients(processed_dir="data/processed", num_clients=5, iid=True):
    """
    Split the global training dataset into M shards for M Federated Learning clients.
    
    Args:
        processed_dir (str): Directory containing the preprocessed X_train.pt and y_train.pt
        num_clients (int): Number of FL clients to split the data for
        iid (bool): If True, split data independently and identically distributed.
                    If False, creates non-IID partitions (e.g., each client gets different attacks).
    """
    print(f"Loading global training data from {processed_dir}...")
    try:
        X_train = torch.load(os.path.join(processed_dir, 'X_train.pt'))
        y_train = torch.load(os.path.join(processed_dir, 'y_train.pt'))
    except FileNotFoundError:
        print("Error: Train tensors not found. Please run preprocess.py first.")
        return
        
    total_samples = len(X_train)
    print(f"Total training samples: {total_samples}")
    
    # We will only split the training data.
    # The global server or evaluation script will use the global X_test.pt / y_test.pt
    
    # Create client directories
    client_dirs = [os.path.join(processed_dir, f"client_{i+1}") for i in range(num_clients)]
    for d in client_dirs:
        os.makedirs(d, exist_ok=True)
        
    if iid:
        print(f"Creating IID splits for {num_clients} clients...")
        # Simple random split
        indices = np.random.permutation(total_samples)
        
        # Split indices into roughly equal chunks
        split_indices = np.array_split(indices, num_clients)
        
        for i in range(num_clients):
            client_X = X_train[split_indices[i]]
            client_y = y_train[split_indices[i]]
            
            torch.save(client_X, os.path.join(client_dirs[i], 'X_train.pt'))
            torch.save(client_y, os.path.join(client_dirs[i], 'y_train.pt'))
            
            print(f"Client {i+1} got {len(client_X)} samples.")
    else:
        print(f"Creating Non-IID splits for {num_clients} clients...")
        # Sort by labels to group similar attacks together
        sorted_indices = torch.argsort(y_train)
        
        # Then split into chunks
        split_indices = np.array_split(sorted_indices, num_clients)
        
        for i in range(num_clients):
            client_X = X_train[split_indices[i]]
            client_y = y_train[split_indices[i]]
            
            torch.save(client_X, os.path.join(client_dirs[i], 'X_train.pt'))
            torch.save(client_y, os.path.join(client_dirs[i], 'y_train.pt'))
            
            # Print label distribution for this client to verify Non-IID
            unique, counts = np.unique(client_y.numpy(), return_counts=True)
            dist = dict(zip(unique, counts))
            print(f"Client {i+1} got {len(client_X)} samples. Label distribution: {dist}")

    print("Data splitting complete!")

if __name__ == "__main__":
    split_data_for_clients(num_clients=5, iid=True)
