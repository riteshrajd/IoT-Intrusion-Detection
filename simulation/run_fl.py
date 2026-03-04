#!/usr/bin/env python3
import subprocess
import time
import argparse
import sys
import os

def run_fl_simulation(num_clients=5, rounds=3, model_type="lstm"):
    print("=====================================================")
    print(f"Starting Federated Learning IoT Simulation")
    print(f"Model: {model_type.upper()} | Clients: {num_clients} | Rounds: {rounds}")
    print("=====================================================\n")

    processes = []
    
    # Ensure saved_models directory exists
    os.makedirs("saved_models", exist_ok=True)

    # Start the server
    print("[1] Starting FL Server...")
    server_cmd = [
        sys.executable, "src/server/fl_server.py",
        "--rounds", str(rounds),
        "--min-clients", str(num_clients),
        "--model-type", model_type
    ]
    server_process = subprocess.Popen(server_cmd)
    processes.append(server_process)

    # Wait for server to initialize
    time.sleep(3)

    # Start clients
    print(f"[2] Starting {num_clients} IoT Clients...")
    for i in range(num_clients):
        client_id = i + 1
        client_cmd = [
            sys.executable, "src/client/iot_client.py",
            "--client-id", str(client_id),
            "--model-type", model_type
        ]
        # Start the client process
        p = subprocess.Popen(client_cmd)
        processes.append(p)
        time.sleep(1) # Stagger client start slightly
        
    print(f"\n[3] Simulation running. Waiting for {rounds} FL rounds to complete...\n")
    
    try:
        # Wait for all processes to complete
        # Technically we only need to wait for the server, as it will close when rounds finish
        server_process.wait()
        
        # Kill clients when server finishes
        for p in processes[1:]:
            p.terminate()
            
    except KeyboardInterrupt:
        print("\nShutting down FL simulation...")
        for p in processes:
            p.terminate()
            
    print("\n=====================================================")
    print("Simulation execution complete.")
    print("Check saved_models/ for the global aggregated model.")
    print("=====================================================")

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Run FL Simulation")
    parser.add_argument("--clients", type=int, default=5, help="Number of FL clients to simulate")
    parser.add_argument("--rounds", type=int, default=3, help="Number of FL communication rounds")
    parser.add_argument("--model-type", type=str, default="lstm", choices=["lstm", "gru"], help="Model type")
    
    args = parser.parse_args()
    run_fl_simulation(args.clients, args.rounds, args.model_type)
