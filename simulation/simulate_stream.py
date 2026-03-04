#!/usr/bin/env python3
import time
import os
import torch
import numpy as np
import collections
import sys
from tqdm import tqdm

# Add parent dir to path so we can import from src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.models.ids_model import get_model

# Constants
SEQ_LENGTH = 10
DELAY = 0.05  # Faster wait between simulated packets (for visualization)

def log_detection(packet_idx, prediction, confidence, classes):
    """Print the detection result with formatting for the simulated dashboard."""
    pred_class = classes[prediction]
    
    # ANSI Color Codes
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'
    
    if pred_class.lower() == 'benign':
        status = f"{GREEN}[CLEAR] Benign Traffic{RESET}"
        is_attack = False
    else:
        status = f"{RED}[ALERT] IMMINENT {pred_class.upper()} ATTACK DETECTED!{RESET}"
        is_attack = True
        
    print(f"Packet Window #{packet_idx:05d} | {status} | Confidence: {confidence*100:.2f}%")
    return is_attack

def simulate_realtime_stream(model_path, data_path, classes_path, model_type="lstm"):
    """Simulate a real-time stream of IoT network packets and detect intrusions."""
    
    print(f"Loading global model from {model_path}...")
    device = torch.device("cpu") # Real-time inference usually fine on CPU
    model = get_model(model_type=model_type, input_size=46, hidden_size=64, num_classes=8, num_layers=1)
    
    try:
         # Load the state dict
        state_dict = torch.load(model_path, map_location=device)
        model.load_state_dict(state_dict)
    except Exception as e:
        print(f"Error loading model: {e}")
        print("Please ensure the global model exists (run the FL simulation first).")
        return
        
    model.eval()
    
    # Load class mappings
    try:
        classes = np.load(classes_path, allow_pickle=True)
    except FileNotFoundError:
        print(f"Error: Classes file {classes_path} not found.")
        return

    # For simulation, we'll pretend the test dataset represents the streaming real-time data
    print(f"Loading test stream data from {data_path}...")
    try:
        # Load the Raw X sequences directly for simulation (to save time, we already generated sequences)
        # In a TRUE real-time script, we would load single packet feature vectors from a CSV line by line,
        # fill a deque of maxlen=10, and then infer. Here we'll just iterate over the pre-built test sequences 
        # to simulate time passing.
        X_stream = torch.load(os.path.join(data_path, 'X_test.pt'))
        # y_stream = torch.load(os.path.join(data_path, 'y_test.pt')) # Ground truth (optional, for comparing)
    except FileNotFoundError:
        print("Error: Test data not found.")
        return
    
    print("\n" + "="*60)
    print("🚀 INITIALIZING REAL-TIME IoT INTRUSION DETECTION DASHBOARD 🚀")
    print("="*60 + "\n")
    
    # Simulate more stream sequences
    num_to_simulate = args.packets
    
    # Add a slight delay before starting
    time.sleep(1)
    
    
    # Track statistics
    total_packets = min(num_to_simulate, len(X_stream))
    attacks_deflected = 0
    benign_passed = 0
    
    # We will pick a random slice to simulate, so it's not always the exact same first N sequences
    start_idx = np.random.randint(0, max(1, len(X_stream) - total_packets))

    with torch.no_grad():
        for i in range(total_packets):
            # Extract sequence (shape: [1, seq_len, features])
            sequence = X_stream[start_idx + i].unsqueeze(0).to(device)
            
            # Inference
            start_time = time.time()
            output = model(sequence)
            probabilities = torch.nn.functional.softmax(output, dim=1)
            
            conf, pred = torch.max(probabilities, 1)
            
            # Log Detection
            is_attack = log_detection(i+1, pred.item(), conf.item(), classes)
            
            if is_attack:
                attacks_deflected += 1
            else:
                benign_passed += 1
                
            # Simulate real-time delay
            time.sleep(DELAY)
            
    # Calculate percentages
    attack_percent = (attacks_deflected / total_packets) * 100 if total_packets > 0 else 0
    benign_percent = (benign_passed / total_packets) * 100 if total_packets > 0 else 0
            
    print("\n" + "="*60)
    print("📈 FINAL INTRUSION DETECTION SUMMARY 📈")
    print("="*60)
    print(f"Total Traffic Windows Analyzed: {total_packets}")
    print(f"Benign Traffic Passed:          {benign_passed} ({benign_percent:.2f}%)")
    print(f"Malicious Attacks Deflected:    {attacks_deflected} ({attack_percent:.2f}%)")
    print("="*60 + "\n")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser("IoT IDS Simulation")
    parser.add_argument("--model-path", type=str, required=True, help="Path to global model .pth file")
    parser.add_argument("--model-type", type=str, default="lstm", choices=["lstm", "gru"], help="Model type")
    parser.add_argument("--packets", type=int, default=500, help="Number of packets to simulate")
    args = parser.parse_args()
    
    simulate_realtime_stream(
        model_path=args.model_path,
        data_path="data/processed",
        classes_path="data/processed/classes.npy",
        model_type=args.model_type
    )
