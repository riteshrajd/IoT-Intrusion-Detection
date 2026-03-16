### **Sr No.**

3

### **Title**

Privacy-Preserving Federated Learning for Intrusion Detection in IoT Environments: A Survey 

### **Contribution (What the paper gives us)**

This paper acts as the ultimate defensive playbook for your system. It comprehensively surveys the attack vectors that target Federated Learning (FL) directly—such as hackers stealing data from model weights—and details the cryptographic shields and software frameworks needed to secure Intrusion Detection Systems (IDS) in the Internet of Things (IoT).

### **Methodology & Techniques**

* 
**Privacy-Preserving Mechanisms (PPMs):** Differential Privacy (DP), Homomorphic Encryption (HE), Secure Multi-Party Computation (SMPC), Trusted Execution Environments (TEE), and Blockchains.


* 
**Federated Learning Types:** Horizontal FL (HFL), Vertical FL (VFL), Federated Transfer Learning (FTL), Cross-Device FL, and Cross-Silo FL.


* 
**Attack Vectors on FL:** Poisoning Attacks (Data and Model), Inference Attacks, Data Reconstruction, Evasion Attacks, and Backdoor Attacks.


* 
**Aggregation Algorithms:** `FedAvg` (Federated Averaging), `FedProx` (handles statistical heterogeneity/Non-IID data), `FedPAQ`, `FedMA`.



### **Frameworks (How to code it)**

You do not need to code the FL architecture from scratch. The paper evaluates several open-source Application Programming Interfaces (APIs):

* **Flower (flwr):** Highly recommended. It is user-friendly, actively maintained, and works seamlessly with PyTorch. In the paper's experiments, it achieved the highest accuracy.


* **TensorFlow Federated (TFF):** Google's framework. It is slightly harder to use but offers strong, native support for Differential Privacy (DP) mechanisms.


* 
**FATE:** Best for Vertical FL (VFL) scenarios.


* 
**Others evaluated:** FedML, Substra, OpenFL, PySyft, PaddleFL, IBM-FL, FederatedScope.



### **Datasets Mentioned**

* 
**For Framework Benchmarking:** MNIST.


* 
**For Modern IoT/IDS Testing:** Edge-IIoTset, InSDN , TON-IoT , BoT-IoT , NSL-KDD, KDD-CUP99, UNSW-NB15 , CSE-CIC-IDS2018, MQTTset.



### **Validation Metrics (Matrices)**

To prove the system works and is efficient, the following metrics are tracked:

* Accuracy, False Alarm Rate (FAR), and Detection Rate (DR).


* Total training time, loss values, CPU usage, and RAM usage.


* 
**Privacy Budget ($\epsilon$):** Used to measure how much Differential Privacy noise is added to the system.



### **Formulas (The Math Behind the Shields)**

* 
**The Global FL Objective (Loss Minimization):** The mathematical goal of the server is to minimize the loss $f(\omega)$ across all $n$ clients:



$$\min_{\omega\in\mathbb{R}^{d}}f(\omega)=\frac{1}{n}\sum_{i=1}^{n}f_{i}(\omega)$$





* 
**Global Differential Privacy (DP):** A mathematical guarantee that adding noise protects the database. It satisfies $\epsilon$-DP if:



$$\frac{P[M(D) \in S]}{P[M(D') \in S]} \le \exp(\epsilon)$$





* 
**Local Differential Privacy (LDP):** The noise is added directly by the $n^{th}$ participant before sending it to the server:



$$\frac{P[M_n(D_n) \in S_n]}{P[M_n(D'_n) \in S_n]} \le \exp(\epsilon_n)$$






### **How to Utilize in FL-IDS Project**

* 
**Threat Modeling:** Dedicate a section to "Model Poisoning" to prove you understand that standard FL is vulnerable to compromised edge routers sending malicious weights.


* 
**Implementation:** Build your system using the **Flower** framework and PyTorch.


* **Applying Armor:** Implement **Local Differential Privacy (LDP)**. Add mathematical noise to your model weights on the client-side *before* transmitting them to the central server to stop Model Inversion attacks.


* 
**Aggregation Upgrade:** If your data is highly imbalanced across clients (Non-IID), swap your server's aggregation math from `FedAvg` to `FedProx` to maintain stability.



### **Outcome / Takeaway**

* 
**The Privacy vs. Accuracy Trade-off:** Adding cryptographic armor degrades the AI's performance. The paper's experiments prove that a standard `FedAvg` model achieved 98.90% accuracy, but when Differential Privacy ($\epsilon=0.001$) was turned on, accuracy dropped to 89.98%. You must explicitly mention this trade-off in your project.



### **Open Issues (How to make your project stand out)**

* **Communication Overhead:** FL requires sending massive matrices of weights. Mentioning techniques like model compression (quantization) to save IoT bandwidth will highly impress evaluators.


* 
**Non-IID Data Heterogeneity:** IoT devices generate vastly different data volumes. Addressing this using `FedProx` proves your system can survive in the real world.


* **Zero-Day Attacks:** Supervised AI fails against unseen threats. Combining PPFL with anomaly detection to catch brand-new attacks is a massive, unsolved challenge.



### **Important Figures / Tables to Note**

* 
**Figure 2 & 3 (Page 7):** Visual breakdown of how Differential Privacy works (Local vs. Global).


* 
**Figures 7 through 10 (Pages 15-16):** The actual performance graphs proving exactly how much accuracy drops when Differential Privacy is activated. Use these as visual evidence for the privacy/accuracy trade-off.


* 
**Table 5 & 6 (Pages 23-24):** The ultimate cheat sheets showing exactly what AI algorithms, PPMs, and datasets other researchers combined to build their systems.