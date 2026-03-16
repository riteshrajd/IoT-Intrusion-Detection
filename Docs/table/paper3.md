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