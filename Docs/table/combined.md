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
