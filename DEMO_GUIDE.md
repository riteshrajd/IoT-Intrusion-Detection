# IoT Intrusion Detection (Federated Learning)
**Project Demo Guide**

This project simulates a Federated Learning (FL) environment where multiple IoT devices collaboratively train an Intrusion Detection System (IDS) using a Recurrent Neural Network (LSTM/GRU) on Sequential network traffic data.

---

## 🚀 How To Run The Full Training Demo (From Scratch)

If you want to show the entire pipeline from processing the raw data to training the Federated model across multiple devices:

1. **Activate Environment:**
   Ensure you are in the project folder and the virtual environment is active.
   ```bash
   source .venv/bin/activate
   ```

2. **Process and Split Data:**
   Convert the raw CSV into Time-Series sequences, balance the classes, and shard the data for 5 IoT clients.
   ```bash
   python src/data_utils/preprocess.py
   python src/data_utils/data_splitter.py --clients 5
   ```

3. **Run Federated Learning Cluster:**
   Spin up the FL Server and 5 IoT Clients simultaneously to train the `gru` model over 3 communication rounds.
   ```bash
   python simulation/run_fl.py --clients 5 --rounds 3 --model-type gru
   ```
   *(This will save the final aggregated model to `saved_models/global_gru_round_3.pth`)*

4. **Run Real-Time Dashboard Simulation:**
   Feed simulated real-time packet windows into the newly trained global model to watch it detect attacks.
   ```bash
   python simulation/simulate_stream.py --model-path saved_models/global_gru_round_3.pth --model-type gru --packets 250
   ```

---

## ⚡ How To Run Just The Simulation (Using Pre-Trained Model)

If you don't have time to run the heavy training process during the presentation and just want to show the **Real-Time Detection Dashboard** working:

1. **Ensure Environment is Active:**
   ```bash
   source .venv/bin/activate
   ```

2. **Run The Streamer:**
   We have already saved a fully verified, pre-trained GRU model exactly for this purpose (`local_verified_gru.pth`).
   ```bash
   python simulation/simulate_stream.py --model-path saved_models/local_verified_gru.pth --model-type gru --packets 500
   ```
   *(You can change `--packets 500` to whatever number of sequences you want to simulate).*

---

## 📊 Understanding The Results (Why so many attacks?)

During the simulation, you might see a summary like this:
```text
Total Traffic Windows Analyzed: 200
Benign Traffic Passed:          7 (3.50%)
Malicious Attacks Deflected:    193 (96.50%)
```

**Question:** Is this heavily skewed 96% Attack vs 3% Benign ratio due to the dataset being unbalanced?

**Answer:** **Yes! Absolutely.** 
The original `IoT_Intrusion.csv` dataset contains 1.04 Million specific "Attack" packets, but only 19,500 "Benign" (Normal) packets. **That means the raw dataset is 98% Attacks and 2% Normal traffic.**

During the `preprocess.py` phase, we internally balanced the *Training Data* (undersampling the attacks) so the Artificial Intelligence wouldn't just become "lazy" and guess "Attack" every time. We forced the AI to mathematically learn the *differences* between the packets.

However, during the `simulate_stream.py` execution, we are feeding the model the **Raw Test Data Stream**. Because the real-world dataset provided by the researchers is essentially a giant recording of a massive DDoS/Mirai botnet attack, when we simulate reading from it sequentially, the vast majority of the packets flowing through the network *are indeed real attacks*. 

So when the AI detects 193 attackers and only 7 benign users, it is **accurately reflecting the severe threat environment of the dataset**.
