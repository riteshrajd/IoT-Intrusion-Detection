# Federated Learning for IoT Intrusion Detection

## 📌 Project Overview
The **IoT Intrusion Detection** project simulates a secure, privacy-preserving environment where multiple Internet of Things (IoT) devices collaboratively train an Artificial Intelligence model to detect network cyberattacks. 

Instead of sending raw, sensitive network traffic to a centralized server (which poses privacy and bandwidth concerns), this project uses **Federated Learning**. Each IoT device trains a local model on its own data, and only the mathematical "learnings" (model weights) are sent to the central server to create a global, super-smart Intrusion Detection System (IDS).

---

## 💾 The Data 
The project uses a comprehensive IoT Network Intrusion dataset (`IoT_Intrusion.csv`). 

- **Features:** Every packet flowing through the network is analyzed across 46 statistical features (e.g., flow duration, header length, connection rates, and TCP/UDP flags).
- **Classes:** The raw data contains 34 specific sub-attacks which our pipeline groups into 8 main categories for clear classification:
  - `Benign` (Normal, safe traffic)
  - `DDoS` (Distributed Denial of Service)
  - `DoS` (Denial of Service)
  - `Mirai` (IoT Botnet traffic)
  - `Spoofing`
  - `Recon` (Reconnaissance / scanning)
  - `Web-based`
  - `Brute Force`

### Data Preprocessing      
Because Network traffic is a continuous stream of events, looking at a single packet isolation isn't enough to detect complex attacks. 
1. **Sequencing:** We buffer the data into **sliding time-windows** (10 packets at a time). This allows the AI to understand the *flow* and *context* of the traffic over time.
2. **Balancing:** Real-world cyberattack datasets often consist of 98%+ malicious packets (like recording a massive DDoS attack). We artificially under-sample the attacks during training so the AI is forced to learn the mathematical differences between normal and malicious traffic, rather than just blindly guessing "Attack" every time.
3. **Scaling:** Features are standardized using `StandardScaler` to ensure the neural networks converge quickly and accurately.

---

## 🧠 How The Model Works
We use **Recurrent Neural Networks (RNNs)**—specifically **LSTM** (Long Short-Term Memory) and **GRU** (Gated Recurrent Unit) architectures.

Unlike standard neural networks, LSTMs and GRUs have internal "memory." When they analyze the current network packet, they remember the context of the previous 9 packets in the window. If they see a sudden, unnatural spike in connection requests compared to the last few milliseconds, the internal gates trigger, and the model flags an impending DDoS or DoS attack.

---

## 🌐 How The Federated Simulation Works

The project uses the `flwr` (Flower) framework to simulate the decentralized ecosystem:

1. **Data Sharding:** The massive, balanced training dataset is chopped into completely separate, non-overlapping subsets.
2. **The Clients (`src/client/iot_client.py`):** We spin up multiple simulated IoT devices (e.g., 5 clients). Each client securely loads its own shard of the dataset and trains a local GRU/LSTM model.
3. **The Server (`src/server/fl_server.py`):** A central coordinator server listens for the clients.
4. **Federated Averaging (FedAvg):** Once the clients finish their local training, they send their mathematical weights (NOT the raw data) to the server. The server averages these weights together to create an upgraded "Global Model".
5. **Rounds:** This process repeats for multiple rounds, constantly making the Global Model smarter without ever centralizing the raw data.

---

## ⏱️ The Real-Time Dashboard
The project includes a Real-Time streaming script (`simulation/simulate_stream.py`). 

It loads the final, globally-trained Federated model and feeds it an unseen, sequential stream of raw network traffic. It simulates a live dashboard, dynamically printing colored alerts the millisecond it detects the mathematical signature of an incoming attack, while letting benign traffic pass.

---

## 🛠️ How To Run The Code
Check out the `DEMO_GUIDE.md` file in this repository for quick, step-by-step terminal commands to run either the full rigorous training pipeline or just the 5-second real-time detection simulation!
