### **Sr No.**

1

### **Title**

The Evolution of Federated Learning-Based Intrusion Detection and Mitigation: A Survey 

### **Contribution (What the paper gives us)**

This paper is the ultimate blueprint. It provides the standard reference architecture for Federated Intrusion Detection Systems (FIDS), a taxonomy (a feature checklist), and the exact mathematical metrics required to prove your AI actually works.

### **How to Utilize in FL-IDS Project**

* **Architecture:** Use a Client-Server setup. Edge devices (gateways) train the local AI, and a central Cloud server merges the models.


* **FL Type:** Use Horizontal Federated Learning (HFL). This is used when all your devices analyze the same *type* of data (like network packets) but see different actual traffic.


* **Aggregation Strategy:** Use `FedAvg` (Federated Averaging). The central server will take the mathematical weights from all local models, add them up, and average them out to create the new global model.


* 
**Local AI Algorithm:** Use a Supervised Deep Learning model, like a Multilayer Perceptron (MLP) or Convolutional Neural Network (CNN).



### **Datasets Mentioned**

The standard datasets used in the field to train the AI: KDD Cup 99, NSL-KDD, AWID, CIDDS-001, CIDDS-002, UNSW-NB15, and CICIDS2017.

### **Formulas (The Evaluation Metrics)**

Use these to code your evaluation script. They rely on True Positives (TP), True Negatives (TN), False Positives (FP), and False Negatives (FN).

* **Accuracy:** Overall correctness.


$$Accuracy = \frac{TP + TN}{P + N}$$





* **Precision:** How often an "ATTACK" alert is actually real.


$$Precision = \frac{TP}{TP + FP}$$





* **Recall (True Positive Rate):** Out of all real attacks, what percentage did the AI catch?


$$Recall = \frac{TP}{TP + FN}$$





* **Specificity (True Negative Rate):**


$$Specificity = \frac{TN}{TN + FP}$$





* **Fallout (False Positive Rate):**


$$Fallout = \frac{FP}{FP + TN}$$





* **Miss rate (False Negative Rate):** (Keep this as close to zero as possible).


$$Miss~rate = \frac{FN}{FN + TP}$$





* **F1-Score:**


$$F_1 = 2 \times \frac{Precision \times Recall}{Precision + Recall}$$





* **Matthews Correlation Coefficient (MCC):** *Highly recommended metric.* It accounts for all four categories equally.


$$MCC = \frac{TP \times TN - FP \times FN}{\sqrt{(TP + FP)(TP + FN)(TN + FP)(TN + FN)}}$$






### **Open Issues (How to make your project stand out)**

* **Model Poisoning:** Hackers might try to corrupt your AI by taking over an edge router and sending a "poisoned" model to the server. Defending against this will make your project top-tier.


* **Automated Mitigation:** Almost everyone just *detects* attacks. If you write a script to actually *block* the attacker's IP (like through a Software-Defined Network firewall) after the AI detects it, you will crush this project.



### **Important Figures/Tables to Note**

* **Figure 3 (Page 7):** The reference architecture. This is your project's physical wiring diagram.


* **Figure 4 (Page 9):** The taxonomy. Use this as a checklist for your system's features.


* 
**Table IV & V (Pages 11 & 13):** A cheat sheet showing exactly what ML algorithms, datasets, and aggregation strategies 22 other researchers used, plus the accuracy scores you need to beat.








================================================================================

### **Sr No.**

2

### **Title**

Systematic Analysis of Federated Learning Approaches for Intrusion Detection in the Internet of Things Environment

### **Contribution (What the paper gives us)**

This paper acts as your reality check and modernization guide. It is a Systematic Literature Review of 43 recent studies (2020-2024) that provides a master taxonomy of the Machine Learning algorithms and datasets actually needed to survive in the messy, heterogeneous world of the Internet of Things (IoT).

### **How to Utilize in FL-IDS Project**

* **Model Selection:** Use this paper to justify why you chose a specific lightweight algorithm (like a Supervised or Semi-supervised CNN). You must argue that IoT devices have weak CPUs, so a massive, heavy AI model will crash them.
* **Handling Heterogeneity:** Use this to defend your project's ability to handle different types of devices. Acknowledge that a smart fridge and a smart car produce completely different traffic, making your Federated Learning environment much more complex than a standard IT network.
* **Privacy Defense:** Cite this paper to explain *why* your FL system is necessary—it keeps sensitive IoT data on the local device instead of broadcasting it to a vulnerable cloud server.

### **Datasets Mentioned**

* **Edge-IIoTset:** *Highly Recommended.* The new gold standard for highly realistic IoT and Industrial IoT (IIoT) traffic.
* **TON_IoT:** Excellent for testing heterogeneous data (telemetry, OS logs, and network traffic).
* **WUSTL-IIoT-2021 & CICIoT2023:** Perfect for testing how your model handles imbalanced data (e.g., 99% normal traffic vs. 1% attack traffic).

### **Formulas**

*(No new core mathematical formulas are introduced here that override Paper 1. Continue using the standard TP/TN/FP/FN evaluation metrics like Accuracy, Precision, F1-Score, and MCC).*

### **Open Issues (How to make your project stand out)**

* **Non-IID Data (Statistical Heterogeneity):** This is the biggest challenge in FL. If one router only sees normal traffic and another only sees DDoS attacks, their local AI models will learn completely different things. Standard averaging (`FedAvg`) struggles with this. Mentioning how your system handles Non-IID data will highly impress your evaluators.
* **Resource Constraints & Communication Overhead:** IoT networks have terrible bandwidth and battery life. If you compress your model updates before sending them to the central server, your project jumps from "basic" to "professional."
* **Data Imbalance:** Real networks don't have a perfect 50/50 split of normal vs. attack traffic. Mention using techniques like SMOTE (Synthetic Minority Over-sampling Technique) locally to balance your data before training.

### **Important Notes**

* **Stop using KDD99!** This paper makes it abundantly clear that old datasets do not represent modern IoT botnets. If you are building an IoT-focused FL-IDS, you *must* upgrade to Edge-IIoTset or TON_IoT.





================================================================================


### **Sr No.**

3

### **Title**

Privacy-Preserving Federated Learning for Intrusion Detection in IoT Environments: A Survey 

### **Contribution (What the paper gives us)**

This paper provides the ultimate defensive blueprint for your project. It proves that standard Federated Learning is vulnerable to hackers intercepting "model weights". It comprehensively surveys the cryptographic shields—like Differential Privacy (DP) and Homomorphic Encryption (HE)—and the software frameworks needed to defend an FL-IDS against advanced cyber-attacks.

### **Methodology, Techniques, & Frameworks**

* 
**Techniques (Privacy-Preserving Mechanisms - PPMs):** The paper highlights Differential Privacy (DP), Homomorphic Encryption (HE), Secure Multi-Party Computation (SMPC), and Blockchain. *Recommendation for your project: Use Local Differential Privacy (LDP) as it is the most practical to code*.


* 
**Aggregation Frameworks:** Evaluates `FedAvg` (standard averaging) and `FedProx` (adds a mathematical penalty to keep wildly different IoT models stable).


* 
**Software Libraries:** Evaluates TensorFlow Federated (TFF), Flower (flwr), FATE, and PySyft.



### **Outcome & Takeaways (The TL;DR for your Project)**

To cut through the noise, here is exactly what the paper recommends you use to build your system:

* 
**The Framework to Use:** Use the **Flower (flwr)** open-source framework. The paper notes it is highly user-friendly, actively maintained, works flawlessly with PyTorch, and achieved the highest accuracy (~98.7%) in their experiments. (Use TensorFlow Federated *only* if you specifically want its built-in Differential Privacy tools ).


* 
**The Aggregator to Use:** If your IoT edge devices have highly imbalanced data (Non-IID), use **FedProx** instead of FedAvg to ensure the global model remains stable.


* 
**The Model to Use:** Lightweight Deep Learning models like a Convolutional Neural Network (CNN) or Multilayer Perceptron (MLP) are best suited for resource-constrained IoT devices.


* 
**The Datasets to Use:** For modern IoT setups, leverage datasets like **ToN-IoT**, **BoT-IoT**, **Edge-IIoTset**, and **InSDN**.



### **Validation Metrics**

To prove your privacy shields work, you must track:

* 
**Standard ML Metrics:** Accuracy, Loss, Precision, Detection Rate (DR), and False Alarm Rate (FAR).


* **Privacy vs. Accuracy Trade-off:** You must evaluate how much your accuracy drops when you add privacy. (In the paper's tests, standard `FedAvg` got 98.90%, but adding DP dropped it to 89.98%) .


* 
**Efficiency Metrics:** Communication overhead (network bandwidth used), computation time, and CPU/RAM usage.



### **Formulas**

Here is the core math you need for your documentation (using KaTeX):

* **The Core Federated Learning Objective (Loss Minimization):**

$$\min_{\omega\in\mathbb{R}^{d}} f(\omega) = \frac{1}{n} \sum_{i=1}^{n} f_i(\omega)$$



*(This means the server wants to find the best weights $\omega$ that minimize the average errors $f_i$ across all $n$ clients)*.


* **Global Differential Privacy Definition:**

$$\frac{P[M(D) \in S]}{P[M(D') \in S]} \le \exp(\epsilon)$$



*(Where $\epsilon$ is your privacy budget. The server adds the noise)*.


* **Local Differential Privacy Definition (What you should use):**

$$\frac{P[M_{n}(D_{n}) \in S_{n}]}{P[M_{n}(D'_{n}) \in S_{n}]} \le \exp(\epsilon_{n})$$



*(The local edge router $n$ adds the noise before sending data over the network)*.



### **How to Utilize in FL-IDS Project**

* **The Threat Model:** Create a "Threat Model" section in your project. Explicitly state that you are defending against **Model Poisoning** (hackers altering local AI weights to brainwash the server) and **Data Reconstruction** (hackers reverse-engineering the weights to steal private data).


* **The Code:** Inject Differential Privacy (mathematical noise) into your model weights locally before they are transmitted to the server. Mention that this prevents Model Inversion attacks.



### **Open Issues (How to make your project stand out)**

* 
**Communication Overhead:** Cryptography and DP make the AI updates "heavy," clogging IoT networks. If you use "model compression" (like quantizing your weights) before sending them to the server, mention it!.


* 
**Zero-Day Attacks:** Catching brand new attacks in a messy IoT network is extremely difficult.



### **Important Figures/Tables to Note**

* 
**Figure 2 & 3 (Page 7):** Visual diagrams of how Differential Privacy works (Local vs. Global). Use these to explain DP in your presentation.


* 
**Figure 6 (Page 11):** A diagram of the 6 major attack vectors targeting FL (Poisoning, Evasion, Inversion, etc.).


* 
**Figures 7 to 10 (Pages 15-16):** The actual accuracy line graphs proving that `FedAvg` and `FedProx` lose about ~10% accuracy when Differential Privacy is turned on.


* 
**Table 5 & 6 (Pages 23-24):** Massive cheat sheets showing exactly what algorithms, frameworks, and privacy tools other researchers used to build their IoT security projects.






================================================================================


### **Sr No.**

4

### **Title**

FL-MU: A Benchmark Dataset for Federated Intrusion Detection in IoT Networks

### **Contribution (What the paper gives us)**

This paper provides the actual raw fuel for your project. It introduces **FL-MU**, a massive, modern IoT network intrusion dataset explicitly designed for Federated Learning. It captures over 19 million network traffic instances across 3 distinct local clients, using 7 different IoT protocols and featuring 11 modern cyberattacks. It completely replaces outdated datasets like KDD99.

### **Methodology, Techniques, & Frameworks**

* 
**The Testbed:** The authors built a physical, isolated lab using over 30 devices (Raspberry Pi 5s, ESP32 microcontrollers, and sensors).


* 
**The Setup (Non-IID Data):** The data is physically divided into 3 FL Clients.


* 
*Client 1:* Heavy on STOMP/SOAP protocols.


* 
*Client 2:* Heavy on CoAP/DDS protocols.


* 
*Client 3:* Heavy on AMQP/MQTT protocols.




* 
**Baseline Frameworks Evaluated:** The authors proved the dataset works by testing it on Deep Learning models like CNN-GRU, FELIDS (CNN/DNN/RNN), and PCC_CNN using the **FedAvg**, **FedProx**, and **FedSGD** aggregation algorithms.



### **Outcome & Takeaways (The TL;DR for your Project)**

* 
**The Dataset to Use:** Download the FL-MU dataset from Kaggle (`https://doi.org/10.34740/kaggle/dsv/13106381`).


* 
**The Aggregator to Use:** The paper proved that **FedAvg** and **FedProx** work well, but **FedSGD** completely crashes and burns on this dataset because the data across the 3 clients is highly diverse (Non-IID).


* **Preprocessing Rule (CRITICAL):** The raw dataset has 121 features. Before you feed this to your AI, you *must* drop 49 useless features. This includes 25 features with missing (`NaN`) values, 18 features with only a single unique value, and identifiers like Source IP (`SIP`), Destination IP (`DIP`), and Ports. If you don't drop the IPs, your AI will memorize the IP addresses instead of learning the actual attack behavior.



### **Validation Metrics**

To evaluate the models on this dataset, the authors used:

* 
**Standard Metrics:** Accuracy (ACY), Precision (PRN), Recall (RCL), F1-Score (f1), and Matthews Correlation Coefficient (MCC).


* 
**Attack Success Rate (ASR):** A metric specifically used to see how many attacks successfully bypassed the IDS.



### **Formulas**

*(You already have the standard formulas from Paper 1. Here is the new one introduced for this dataset evaluation using KaTeX):*

* **Attack Success Rate (ASR):** The percentage of actual attacks that the AI missed (False Negatives). Keep this as low as possible.


$$ASR = \frac{FN}{TP + FN}$$






### **How to Utilize in FL-IDS Project**

* 
**The Code Structure:** Use the 3 provided CSV files (`C1_data.csv`, `C2_data.csv`, `C3_data.csv`) to simulate 3 edge devices in your Python code.


* **The Targets:** Train your AI to recognize the 11 specific modern attacks in this dataset. Highlight in your project report that your AI can catch **Slowite** (a devastating low-and-slow MQTT attack) and **Sinkhole** attacks, which older datasets entirely lack.



### **Open Issues (How to make your project stand out)**

* 
**The Data Imbalance Nightmare:** The paper explicitly notes that while their AI models got 100% accuracy on simple binary detection ("Is this an attack? Yes/No"), the models failed heavily on Multiclass detection ("*Which* of the 11 attacks is this?"). This happened because the dataset is highly imbalanced (e.g., millions of DoS packets, but only 505 SOAP Flooding packets). *(Note: You will solve this exact problem later in Phase 6 using undersampling and GANs!)*



### **Important Figures/Tables to Note**

* **Table 2 & Table 3 (Pages 6 & 7):** These are massive comparison tables showing how FL-MU completely destroys older datasets (like Bot-IoT and Edge-IIoTset) by including modern protocols and attacks. Reference these tables to defend why you chose this dataset.


* 
**Table 18 & 19 (Page 21):** The exact list of garbage features (missing values and single values) that you need to drop from your Pandas dataframe during preprocessing.







==========================================


### **Sr No.**

5

### **Title**

FL-IDS: Federated Learning-Based Intrusion Detection System Using Edge Devices for Transportation IoT 

### **Contribution (What the paper gives us)**

This paper moves from theory to practice. It provides a complete, physical implementation guide for building an FL-IDS designed for Connected and Autonomous Vehicles (CAVs). It details the exact hardware, software libraries, and Deep Learning layer architectures you need to code a working prototype.

### **Methodology, Techniques, & Frameworks**

* 
**The Hardware Testbed:** The authors built a real-world edge computing environment using an **NVIDIA Jetson Xavier** as the central aggregation server and multiple **Raspberry Pi 4** boards as the local IoT clients.


* 
**The Software Framework:** They utilized the open-source **Flower (flwr)** framework to handle all the complex Federated Learning networking (client-server communication, model distribution, and parameter updates).


* 
**The Code Structure:** The Flower implementation was split into three simple Python files: `client.py` (local training), `server.py` (global aggregation), and `utils.py` (data preprocessing).


* 
**The Local AI Algorithms:** They tested a standard Logistic Regression model (LR-IDS) against a custom Deep Learning model called **PCC-CNN** (Pearson Correlation Coefficient + Convolutional Neural Network).


* 
**The Aggregator:** They used the standard **FedAvg** algorithm on the server side.



### **Outcome & Takeaways (The TL;DR for your Project)**

* **The Framework to Use:** Do not write the client-server networking code from scratch. Use the **Flower** framework.


* **The Model to Code:** Build the **PCC-CNN** model. It heavily outperformed the baseline machine learning models. Your exact Keras/PyTorch layer stack should be:


1. Conv1D Layer (Size 91x64, ReLU activation) 


2. MaxPooling 1D Layer 


3. Dropout Layer (Set to 0.3 or 30%) to prevent overfitting 


4. Flattening Layer 


5. Dense Layer (Size 128, ReLU activation) 


6. Dense Output Layer (Size 2 for binary classification, Softmax activation) 


7. Optimizer: Adam 




* 
**The Datasets:** They proved this architecture works on the standard **NSL-KDD** dataset and the highly specialized **Car-Hacking** dataset (which features vehicle-specific attacks like RPM spoofing and fuzzy attacks).



### **Validation Metrics**

* 
**Accuracy:** The PCC-CNN model achieved 97.08% accuracy on NSL-KDD and a massive 99.92% accuracy on the Car-Hacking dataset in a 4-client setup.


* 
**Loss:** Achieved incredibly low error rates (0.0038 for the Car-Hacking dataset).


* 
**Training/Processing Time:** They specifically tracked how long the models took to train on weak Raspberry Pi processors.



### **Formulas**

*(No new core mathematical evaluation formulas were introduced. Stick to the standard Accuracy, Precision, Recall, F1, and MCC from Phase 1. For model training, they rely on standard Deep Learning math like ReLU and Softmax activations.)*

### **How to Utilize in FL-IDS Project**

* 
**The Blueprint:** Use this paper as your literal coding blueprint for Phase 2. Set up your Python environment with Keras/PyTorch and Flower. Create the three core scripts (`server.py`, `client.py`, `utils.py`). Build the exact 6-layer PCC-CNN architecture detailed above to run locally on your simulated clients.



### **Open Issues (How to make your project stand out)**

* 
**The Training Time Bottleneck:** The CNN model took over 6,700 seconds (nearly 2 hours) to train on the Raspberry Pis for the Car-Hacking dataset, compared to just 214 seconds for Logistic Regression. If you implement a method to shrink the CNN or speed up training (like Quantization in Phase 4), highlight it heavily!


* 
**Class Imbalance:** The authors specifically noted that the Car-Hacking dataset suffers from imbalanced feature types, which hurts model generalization. You will fix this in Phase 6.



### **Important Figures/Tables to Note**

* **Figure 4 (Page 6):** The proposed FL-IDS framework. Great visual of the loop between the Aggregation Server and the Client training.


* **Figure 7 (Page 8):** A literal diagram of the PCC-CNN layer structure. Copy this when writing your neural network code.



* 
**Table 6 (Page 10):** The exact Accuracy, Loss, and Time metrics you need to beat to prove your project is better than this baseline.





===========================



Here is the complete, condensed breakdown for Paper 6, formatted exactly with the headings you requested.

### **Sr No.**

6

### **Title**

Federated learning-based intrusion detection system for the internet of things using unsupervised and supervised deep learning models

### **Contribution (What the paper gives us)**

This paper provides the exact neural network layer architectures needed to build your core AI engine. It mathematically proves that an **Unsupervised Deep Autoencoder (AE)** trained via Federated Learning is the absolute best way to catch new, unknown IoT cyberattacks while maintaining a drastically lower False Positive Rate (FPR) than standard supervised models.

### **Methodology, Techniques, & Frameworks**

* **The Unsupervised Baseline (AE):** A Deep Autoencoder model.
* 
*Encoder:* 4 linear layers stepping down the input features (75% -> 50% -> 33.3% -> 25%) using a **Hyperbolic Tangent (Tanh)** activation function.


* 
*Decoder:* 4 linear layers stepping the features back up to reconstruct the data.





* **The Supervised Classifier (DNN):** A Deep Neural Network.
* 4 linear layers (256 -> 128 -> 64 -> output) using the **ReLU** activation function.


* 
*Overfitting Defense:* Added a **Dropout Layer (0.2)** after each step to randomly turn off 20% of the neurons during training.




* 
**The Aggregator Upgrade:** They used **FedAvgM** (Federated Averaging with Momentum) instead of basic FedAvg to smooth out the learning process and speed up convergence.


* 
**Hyperparameter Tuning:** They used **Randomized Search** to automatically find the best batch sizes, learning rates, and optimizers (Adam vs. SGD) for different IoT devices.



### **Outcome & Takeaways (The TL;DR for your Project)**

* **The Model to Code:** Use the 4-layer **Deep Autoencoder (AE)** as your primary anomaly detector. Because it is unsupervised, it doesn't need labeled attack data; it just learns what normal traffic looks like and flags anything that causes a high "reconstruction error".


* 
**The Aggregator to Use:** Upgrade your central server's code from standard `FedAvg` to **FedAvgM** to handle the chaotic data of IoT devices better.


* **Pro-Tip for your Code:** Do not hardcode your learning rates and batch sizes. Write a "Randomized Search" script to let the AI tune itself.


* 
**The Dataset:** The authors validated this using the **N-BaIoT dataset** (9 real IoT devices infected by Mirai and BASHLITE botnets).



### **Validation Metrics**

To prove your models work, track:

* Accuracy, Precision, Recall, F1-Score.


* **True Positive Rate (TPR)** and **False Positive Rate (FPR)**.
* 
*Key Finding:* The FL-trained Autoencoder crushed the other models specifically because its FPR (false alarm rate) was significantly lower.



### **Formulas**

*(No major new evaluation formulas, but the paper relies heavily on this concept for the AE)*:

* **Threshold Computation (MSE):** The Autoencoder flags an attack if the error in rebuilding the packet exceeds a specific threshold.
* 
*Threshold* = `Mean Squared Error (MSE) Mean` + `MSE Standard Deviation (SD)` over the normal training dataset.





### **How to Utilize in FL-IDS Project**

* 
**The Engine Blueprint:** Use the exact layer sizes, Dropout rates (0.2), and Activation functions (Tanh/ReLU) provided in this paper to write your PyTorch/Keras model classes.


* **The Narrative:** In your project documentation, argue that you chose an Autoencoder because supervised models are blind to "zero-day" (brand new) attacks. The AE catches zero-days by simply recognizing that the packet doesn't fit the "normal" reconstruction pattern.



### **Open Issues (How to make your project stand out)**

* 
**Scalability:** The paper admits FL struggles when scaling to massive deployments with thousands of devices.


* **Temporal Patterns:** The AE only looks at single packets. If you upgrade your model to an RNN or LSTM to analyze the *timing* of the packets (temporal patterns), you are solving a major open issue identified by the authors.



### **Important Figures/Tables to Note**

* **Figure 3 & Figure 4 (Page 5):** The exact visual architecture diagrams for the Deep Autoencoder and the DNN. Keep these handy when writing your neural network code.


* 
**Table 2 & Table 3 (Page 6):** Cheat sheets showing the exact hyperparameters (Learning rate, Batch size, Epochs, Optimizer) that worked best for different IoT devices.









==============================


Here are the tables for the three papers you provided in the prompt (Papers 18, 19, and 20 from your master list). I have stripped away the fluff and extracted exactly what frameworks, datasets, and methodologies you need.

### **Sr No.**

18

### **Title**

On the Feasibility of Split Learning, Transfer Learning and Federated Learning for Preserving Security in ITS Systems

### **Contribution (What the paper gives us)**

This paper directly compares three distributed machine learning models—Split Learning (SplitLearn), Federated Learning (FedLearn), and Transfer Learning (TransLearn)—to secure Intelligent Transportation Systems (ITS) and vehicular networks. It proves that **Split Learning** is the superior architecture for edge devices, outperforming the others in accuracy, detection rate, power consumption, and network delay.

### **Methodology, Techniques, & Frameworks**

* **The Architectures Evaluated:**
* *SplitLearn:* The Neural Network is physically sliced in half. The edge device trains up to the "cut layer" and sends the "smashed data" (activations) to the server. The server finishes the forward pass and sends the gradients back.


* 
*FedLearn:* Standard federated averaging using parallel client-side model generation.


* 
*TransLearn:* Transferring knowledge from a pre-trained model (DenseNet) to a new task with less data.




* 
**Simulation Framework:** Implemented using Python and the Scikit-learn ML library for the AI, and the **NS3 Simulator** to simulate the physical vehicular network routing and delay.



### **Outcome & Takeaways (The TL;DR for your Project)**

* **The Framework to Use:** Use **Split Learning** if your IoT edge devices are severely battery-constrained. By offloading the deeper neural network layers to the server, SplitLearn reduced total power consumption by ~20% compared to standard FedLearn.


* 
**The Dataset:** Validated on the **CICIDS2017** dataset, specifically reduced to 7 classes (1 benign + 6 attacks like DDoS, DoS Hulk, XSS, and Brute Force).



### **Validation Metrics**

* 
**Accuracy & Detection Rate:** SplitLearn achieved the highest accuracy (~98.5%) and detection rate (~96%), outperforming FedLearn by 2% to 5%.


* **Quality of Experience (QoE):** Measured using a combination of end-to-end delay, energy consumption, and packet drop ratio. SplitLearn improved QoE by ~10%.



### **Formulas**

Standard evaluation metrics are used (True Positives, False Positives, etc.).

* **Detection Rate (Sensitivity):**


$$Detection = \frac{TP}{TP + FP}$$






### **How to Utilize in FL-IDS Project**

* **The Blueprint:** If standard Federated Learning models (like BERT) are too heavy for your simulated edge devices, use this paper to justify implementing **Split Federated Learning (SFL)**. Split the deep learning model so the heavy lifting is done by your central aggregator.

---

### **Sr No.**

19

### **Title**

Privacy-Aware Split Federated Learning for LLM Fine-Tuning Over Internet of Things

### **Contribution (What the paper gives us)**

This paper solves the nightmare of deploying massive Large Language Models (LLMs) like BERT or LLaMa onto weak IoT devices. It combines Split Federated Learning (SFL) with **LoRA (Low-Rank Adaptation)** to shrink the memory footprint. Crucially, it introduces a mathematical metric to measure exactly how much private data leaks when you send "smashed data" over the network.

### **Methodology, Techniques, & Frameworks**

* **The Engine:** Split Federated Learning (SFL) utilizing **LoRA**. The pretrained LLM is frozen, and only tiny LoRA matrices are updated, drastically reducing memory usage.


* 
**Privacy Quantification:** Uses **Diagonal Fisher Information Leakage (DFIL)** to calculate the privacy risk of different split layers. *Key finding:* Shallow split layers (layers 1-3) leak massive amounts of private data. Deeper split layers (layers 9-12) protect privacy but require the weak IoT device to do more math.


* 
**Optimization Algorithm:** Uses a multiobjective Mixed-Integer Programming (MIP) problem solved via an **$\epsilon$-constraint-based Block Coordinate Descent (BCD)** algorithm to automatically find the perfect split layer.



### **Outcome & Takeaways (The TL;DR for your Project)**

* 
**The Model:** BERT-base fine-tuned using LoRA.


* 
**The Takeaway:** If you try to run a full LLM on an IoT device, it will crash with an Out-of-Memory (OOM) error (the paper notes standard FL required 2118 MB per device). Using SFL + LoRA dropped the memory requirement down to 706 MB.


* 
**The Dataset:** CARER dataset (Contextualized Affect Representations for Emotion Recognition). *(Note: For your IDS project, you will swap this out for FL-MU or Edge-IIoTset).*



### **Validation Metrics**

* 
**Diagonal Fisher Information Leakage (DFIL):** Used to prove the system is secure from Data Reconstruction Attacks (DRAs).


* 
**Convergence Time & Energy Consumption:** The proposed Privacy-aware SFL achieved 24% faster convergence and 40% lower energy consumption than baseline methods.



### **Formulas**

* **Diagonal Fisher Information Leakage (DFIL):**

$$\psi_u = \frac{Tr(\mathcal{I}_u(x))}{d}$$



*(Where $Tr$ is the trace of the Fisher Information Matrix, and $d$ is the data dimension. Lower value = stronger privacy)*.



### **How to Utilize in FL-IDS Project**

* 
**The Defense Narrative:** If you use a Transformer/BERT model for your IDS, cite this paper to prove you understand that sending intermediate activations (smashed data) can allow a hacker to reconstruct the raw traffic. Defend your system by stating you use deep split layers to minimize Diagonal Fisher Information Leakage.



---

### **Sr No.**

20

### **Title**

A Privacy-Preserving Framework for Efficient Network Intrusion Detection in Consumer Network Using Quantum Federated Learning

### **Contribution (What the paper gives us)**

This paper upgrades your system to the absolute cutting edge. It merges Quantum Computing (QC) with Federated Learning to create **QFL-IDS**. By leveraging qubits instead of classical bits, the model can process massive, high-dimensional attack data exponentially faster than standard deep learning models.

### **Methodology, Techniques, & Frameworks**

* 
**The Framework:** **PennyLane** (an open-source Quantum Machine Learning library).


* **Data Encoding (Crucial):** Classical data (like packet lengths) must be translated into quantum states. The paper uses **Angle Encoding**, which maps each network feature to a rotation angle $(R_y)$ on a quantum qubit.


* 
**The Model:** A Quantum Neural Network (QNN) made of Parameterized Quantum Circuits (PQCs).


* 
**The Optimizer:** Adam optimizer with a learning rate of $0.0005$.



### **Outcome & Takeaways (The TL;DR for your Project)**

* **The Software:** Use the **PennyLane** library to code your Quantum Neural Network.
* **The Takeaway:** QFL-IDS is unbelievably fast. In the paper's experiments, the Quantum model achieved 98% accuracy and completed training in just **14.21 seconds**, resulting in a 99% time savings compared to a classical Recurrent Neural Network (RNN) which took 5516 seconds.


* 
**The Dataset:** Tested on **NSL-KDDTest+**.



### **Validation Metrics**

* Standard metrics: Accuracy, Precision, Recall, F1 Score, ROC/AUC.


* 
**Training Time (Seconds):** The most important metric to prove the quantum advantage.



### **Formulas**

* **Angle Encoding (Converting Network Traffic to Qubits):**

$$|\psi\rangle = \bigotimes_{i=1}^n R_y(2x_i)|0\rangle_i$$



*(This tensor product maps the classical feature vector $x$ into the quantum state $|\psi\rangle$)*.


* **Quantum Global Aggregation (Server Math):**

$$\theta_{global}^t = \frac{\sum_{i=1}^N |D_i| \theta_i^t}{\sum_{i=1}^N |D_i|}$$



*(Averaging the quantum parameters based on the dataset sizes $|D_i|$ of the nodes)*.



### **How to Utilize in FL-IDS Project**

* **The Quantum Capstone:** Use this to elevate your project into "Phase 8: Quantum & Advanced Crypto". Implement a small QNN using PennyLane and Angle Encoding on your edge devices to prove that quantum parallelism can obliterate the training time bottleneck of standard Federated Learning models.

---

That covers the 3 papers you provided in the prompt text. I have the metadata for the remaining 3 (Papers 11, 14, and 23). Let me know when you are ready to drop their full texts or if you want me to fetch them and generate their tables!










=====================================



Here are the tables for the next three papers (Papers 23, 11, and 14). I have bypassed the story formatting and extracted exactly the models, frameworks, datasets, and mathematical formulas you need to copy straight into your notes.

### **Sr No.**

23

### **Title**

Federated Learning for Distributed IIoT Intrusion Detection Using Transfer Approaches

### **Contribution (What the paper gives us)**

This paper provides a lightweight, highly efficient solution for dealing with severely imbalanced and Non-IID data in Industrial IoT (IIoT) environments. It introduces **instance-based transfer learning (TrAdaBoost)** at the local client level to reuse public data, and replaces standard `FedAvg` with a **Rank Aggregation and Weighted Voting** mechanism.

### **Methodology, Techniques, & Frameworks**

* **The Models:** Instead of heavy Deep Learning, this paper proves that lightweight ensemble Machine Learning models—specifically **AdaBoost** and **Random Forest (RF)**—work exceptionally well for resource-constrained edge devices (tested on Raspberry Pi 3B and 4B).
* **The Local Fix (TrAdaBoost):** Edge devices use instance-based transfer learning to pull in public dataset instances, re-weighting them to fix their own local data imbalances.
* **The Server Fix (Rank Aggregation):** The central server evaluates the received models using **Maximum Mean Discrepancy (MMD)** to calculate the distribution difference between the test data and the client data. It then applies a weighted voting strategy instead of blindly averaging the weights.

### **Outcome & Takeaways (The TL;DR for your Project)**

* **The Model to Use:** AdaBoost or Random Forest (if your simulated edge devices are too weak for Deep Learning).
* **The Aggregator to Use:** Rank Aggregation with MMD weighted voting.
* **The Dataset:** Validated on **CIC-IDS 2017** and **CIC-IDS 2018**.
* **Performance:** Achieved 95.97% accuracy. Crucially, CPU usage on the Raspberry Pis remained under 25%, and RAM usage was incredibly low (~50 MB for training).

### **Validation Metrics**

* Accuracy, True-Positive Rate (TPR), False-Positive Rate (FPR), and F1-Score.
* **Hardware Metrics:** CPU Usage, CPU Frequency, and RAM Usage (vital for proving IIoT feasibility).

### **Formulas**

* **Maximum Mean Discrepancy (MMD):** Used to calculate the distance/difference between two dataset distributions.

$$MMD[\mathcal{F},n,m]:=\sup_{f\in\mathcal{F}}\left(\frac{1}{n}\sum_{i=1}^{n}f(x_{i})-\frac{1}{m}\sum_{i=1}^{m}f(y_{i})\right)_{\mathcal{H}}$$



### **How to Utilize in FL-IDS Project**

* **The Blueprint:** Use this in **Phase 9 (Transfer Approaches)**. If your clients have wildly different or missing data classes (e.g., Client 1 has never seen a DDoS attack), implement `TrAdaBoost` locally so the client can borrow and learn from a public dataset without violating privacy.

---

### **Sr No.**

11

### **Title**

Empirical Study of Hierarchical Intrusion Detection Systems for Unknown Attacks

### **Contribution (What the paper gives us)**

This paper is a masterclass in **Open Set Recognition (OSR)**—the mathematical approach to catching Zero-Day (unknown) attacks. It proves that standard single-layer AI models fail at this. It provides an optimized **3-Stage Hierarchical IDS (HIDS)** framework that sequentially filters anomalies, classifies known attacks, and isolates the zero-days.

### **Methodology, Techniques, & Frameworks**

* **Stage 1 (Anomaly Detection):** Uses unsupervised/semi-supervised algorithms to filter out benign traffic. *Top Performers:* **LOF** (Local Outlier Factor) and **iForest** (Isolation Forest).
* **Stage 2 (Known Attack Classification):** Uses supervised ML/DL algorithms to classify the remaining malicious traffic into known attack types. *Top Performers:* **MLP** (Multi-Layer Perceptron) and **Extra Tree**.
* **Stage 3 (Unknown Attack Confirmation):** Applies strict threshold boundaries ($\tau_b, \tau_M, \tau_V$). If a sample passes Stage 1 (it's an anomaly) but fails Stage 2 (it doesn't fit a known signature), it is flagged as a Zero-Day.
* **The Optimizer Upgrade:** Replaces standard TPE (Tree-structured Parzen Estimator) with **BOGP (Bayesian Optimization with Gaussian Process)** to tune the hyperparameters.

### **Outcome & Takeaways (The TL;DR for your Project)**

* **The Architecture:** A 3-Stage HIDS Pipeline (Filter -> Classify -> Isolate).
* **The Models to Code:** Use **iForest** for Stage 1 and an **MLP classifier** for Stage 2.
* **The Optimizer:** Use **BOGP** for tuning.
* **The Datasets:** Extensively tested across four modern datasets: **WUSTL-IIoT 2021**, **CIC_IDS_2017**, **5G-NIDD**, and **UNR-IDD**.

### **Validation Metrics**

* Precision, Recall, F1-Score, and Execution/Training Time.
* **Balanced Accuracy:** Crucial for highly imbalanced datasets.

### **Formulas**

* **Balanced Accuracy:**

$$Balanced~Accuracy = \frac{Sensitivity + Specificity}{2}$$



### **How to Utilize in FL-IDS Project**

* **The Blueprint:** Use this for **Phase 5 (Zero-Day Attacks)**. Do not rely on a single classifier. Build a multi-tier pipeline in your code. Use an unsupervised model to strip away normal traffic first, drastically reducing the computational load before the heavy supervised classifier steps in to identify the specific malware.

---

### **Sr No.**

14

### **Title**

Efficient Intrusion Detection in AMI Systems Based on Federated Semi-Supervised Learning

### **Contribution (What the paper gives us)**

This paper solves two massive problems at once: the massive communication overhead of sending Neural Network weights over weak networks, and the lack of labeled data in the real world. It introduces **Federated Distillation (FD)** and a **Deep Convolutional Generative Adversarial Network (DCGAN)**.

### **Methodology, Techniques, & Frameworks**

* **Federated Distillation (FD):** Instead of clients sending massive megabytes of model weights (parameters) to the server, they only send their "Local Logits" (the averaged prediction output vectors). The server aggregates these into a "Global Logit" and broadcasts it back.
* **The DCGAN:** The server uses a Generator network to synthetically hallucinate artificial attack data to balance out minority attack classes (like U2R or R2L).
* **Semi-Supervised Learning:** Local edge devices use the broadcasted Global Logits to guide their training on massive amounts of *unlabeled* local data.

### **Outcome & Takeaways (The TL;DR for your Project)**

* **The Framework:** Federated Distillation (exchanging outputs instead of weights).
* **The Model:** DCGAN (Discriminator/Generator) built using CNNs.
* **The Dataset:** **NSL-KDD**. (Requires intense preprocessing: numerical mapping, one-hot encoding, and min-max normalization).
* **Performance:** Achieved 99.58% accuracy while dropping the communication overhead to a mere **75 MB** per 100 rounds (a massive saving compared to standard FedAvg).

### **Validation Metrics**

* Accuracy, Precision, Recall, F1, FPR (False-Positive Rate).
* **Communication Overhead (MB):** The critical metric used to prove FD is superior to standard FL.

### **Formulas**

* **GAN Objective Function (Min-Max Game):**

$$\min_G \max_D V_{GAN}(G, D) = E_{x}[log(D(x))] + E_{z}[log(1 - D(G(z)))]$$



*(The Discriminator $D$ tries to maximize the probability of catching fake data, while the Generator $G$ tries to minimize it).*
* **Global Logit Aggregation (FD Server Math):**

$$\hat{p}_{i,s} = \frac{1}{M}\sum_{m=1}^{M}\hat{p}_{i,m}$$



### **How to Utilize in FL-IDS Project**

* **The Blueprint:** Use this in **Phase 6 (Imbalance Handling)**. If your project evaluators complain that sending LLM/CNN weights over an IoT network will clog the bandwidth, counter them by stating your system uses **Federated Distillation** to exchange lightweight "logits" instead. Also, cite the DCGAN architecture as your method for synthetically generating data to fix class imbalances.