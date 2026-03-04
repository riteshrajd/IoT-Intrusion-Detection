import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
import torch
import os
from tqdm import tqdm

# We will group the 34 sub-attacks into their 8 main parent categories for easier classification
# or we can keep all 34. Let's start with all 34 and encode them.
# The user's list:
ATTACK_MAPPING = {
    'DDoS-ICMP_Flood': 'DDoS',
    'DDoS-UDP_Flood': 'DDoS',
    'DDoS-TCP_Flood': 'DDoS',
    'DDoS-PSHACK_Flood': 'DDoS',
    'DDoS-SYN_Flood': 'DDoS',
    'DDoS-RSTFINFlood': 'DDoS',
    'DDoS-SynonymousIP_Flood': 'DDoS',
    'DDoS-ICMP_Fragmentation': 'DDoS',
    'DDoS-ACK_Fragmentation': 'DDoS',
    'DDoS-UDP_Fragmentation': 'DDoS',
    'DDoS-HTTP_Flood': 'DDoS',
    'DDoS-SlowLoris': 'DDoS',
    
    'DoS-UDP_Flood': 'DoS',
    'DoS-TCP_Flood': 'DoS',
    'DoS-SYN_Flood': 'DoS',
    'DoS-HTTP_Flood': 'DoS',
    
    'Mirai-greeth_flood': 'Mirai',
    'Mirai-udpplain': 'Mirai',
    'Mirai-greip_flood': 'Mirai',
    
    'MITM-ArpSpoofing': 'Spoofing',
    'DNS_Spoofing': 'Spoofing',
    
    'Recon-HostDiscovery': 'Recon',
    'Recon-OSScan': 'Recon',
    'Recon-PortScan': 'Recon',
    'Recon-PingSweep': 'Recon',
    'VulnerabilityScan': 'Recon',
    
    'SqlInjection': 'Web-based',
    'CommandInjection': 'Web-based',
    'Backdoor_Malware': 'Web-based',
    'XSS': 'Web-based',
    'BrowserHijacking': 'Web-based',
    'Uploading_Attack': 'Web-based',
    
    'DictionaryBruteForce': 'Brute Force',
    
    'BenignTraffic': 'Benign'
}

def create_sequences(features, labels, seq_length):
    """
    Convert 2D tabular data into 3D sequence data for LSTM/GRU.
    Shape changes from (N, Features) -> (N - seq_length, seq_length, Features)
    """
    xs, ys = [], []
    for i in tqdm(range(len(features) - seq_length), desc="Creating Sequences"):
        x = features[i:(i + seq_length)]
        # The label for the sequence will be the label of the *last* packet in the window
        y = labels[i + seq_length]
        xs.append(x)
        ys.append(y)
    return np.array(xs), np.array(ys)

def load_and_preprocess_data(input_csv_path, output_dir, seq_length=10, use_main_categories=False):
    print(f"Loading dataset from {input_csv_path}...")
    # Load dataset. We might need to handle large memory. If it crashes, we can use chunks.
    # 1.19M rows is generally fine for pandas on most modern laptops (takes ~1-2GB RAM).
    df = pd.read_csv(input_csv_path)
    
    print(f"Original shape: {df.shape}")
    
    # 1. Handle Missing Values / Inf
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df.fillna(0, inplace=True) # Simple imputation for network traffic
    
    # 2. Extract Labels
    labels = df['label'].values
    
    if use_main_categories:
        print("Mapping 34 subclasses to 8 main categories...")
        # Map labels
        labels = np.array([ATTACK_MAPPING.get(l, 'Unknown') for l in labels])
        
    print("Encoding labels...")
    label_encoder = LabelEncoder()
    encoded_labels = label_encoder.fit_transform(labels)
    
    # Save classes for later use in decoding predictions
    np.save(os.path.join(output_dir, 'classes.npy'), label_encoder.classes_)
    print(f"Found {len(label_encoder.classes_)} classes.")
    
    # 3. Extract Features
    df.drop(columns=['label'], inplace=True)
    features = df.values
    
    # 4. Scale Features
    print("Scaling features using StandardScaler (better for Neural Networks)...")
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    
    # Save the scaler mean/scale for later use (e.g., in inference simulation)
    # Using joblib or pickle is common, but let's do simple numpy saves or just train/test in one go for now
    
    # 5. Create Sequences -> Very computationally heavy for 1M rows.
    # To prevent massive memory usage, we'll save it straight to disk or create sequence subsets.
    print(f"Creating sequences of length {seq_length}...")
    X_seq, y_seq = create_sequences(scaled_features, encoded_labels, seq_length)
    
    # -------------------------------------------------------------
    # CRITICAL FIX: Balance the dataset
    # We discovered 97.6% attacks and only 2.3% benign traffic in this dataset.
    # An IDS needs a balanced dataset to learn accurately instead of just guessing 'Attack'.
    # -------------------------------------------------------------
    print("\nBalancing the dataset (Undersampling majority classes)...")
    # Identify the 'Benign' class index
    try:
        benign_idx = np.where(label_encoder.classes_ == 'Benign')[0][0]
    except Exception:
        # Fallback if mapped differently
        benign_idx = -1
        
    unique_classes, counts = np.unique(y_seq, return_counts=True)
    
    # We will balance to the median count, or cap at 30,000 per class to keep it fast
    target_count = 30000 
    
    balanced_X = []
    balanced_y = []
    
    for cls in unique_classes:
        cls_indices = np.where(y_seq == cls)[0]
        # Undersample if too large
        if len(cls_indices) > target_count:
            np.random.shuffle(cls_indices)
            selected_indices = cls_indices[:target_count]
        else:
            selected_indices = cls_indices
            
        balanced_X.append(X_seq[selected_indices])
        balanced_y.append(y_seq[selected_indices])
        
    X_seq = np.vstack(balanced_X)
    y_seq = np.concatenate(balanced_y)
    
    # Shuffle the final balanced dataset
    shuffle_idx = np.random.permutation(len(X_seq))
    X_seq = X_seq[shuffle_idx]
    y_seq = y_seq[shuffle_idx]
    
    unique_classes, counts = np.unique(y_seq, return_counts=True)
    print(f"Balanced Class Distribution:")
    for c, count in zip(unique_classes, counts):
         print(f"  {label_encoder.classes_[c]}: {count}")
    # -------------------------------------------------------------

    print(f"Final Sequence Shape: {X_seq.shape}")
    print(f"Final Label Shape: {y_seq.shape}")
    
    # 6. Train / Test Split
    print("Splitting data into train and test sets...")
    # Using shuffle=False to respect time-series nature (train on past, test on future)
    X_train, X_test, y_train, y_test = train_test_split(X_seq, y_seq, test_size=0.2, shuffle=False)
    
    # 7. Save Processed Data
    print(f"Saving processed tensors to {output_dir}...")
    torch.save(torch.tensor(X_train, dtype=torch.float32), os.path.join(output_dir, 'X_train.pt'))
    torch.save(torch.tensor(y_train, dtype=torch.long), os.path.join(output_dir, 'y_train.pt'))
    
    torch.save(torch.tensor(X_test, dtype=torch.float32), os.path.join(output_dir, 'X_test.pt'))
    torch.save(torch.tensor(y_test, dtype=torch.long), os.path.join(output_dir, 'y_test.pt'))
    
    print("Preprocessing completed successfully!")

if __name__ == "__main__":
    RAW_DATA_PATH = "data/raw/IoT_Intrusion.csv"
    OUTPUT_DIR = "data/processed"
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # For now, we'll map to the 8 main categories to make the model training a bit faster and more robust
    # User can toggle `use_main_categories=False` if they want the massive 34-class classification.
    load_and_preprocess_data(RAW_DATA_PATH, OUTPUT_DIR, seq_length=10, use_main_categories=True)
