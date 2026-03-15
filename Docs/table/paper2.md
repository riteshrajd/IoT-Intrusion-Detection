Here is the complete, stripped-down breakdown for the second paper, formatted exactly like the first one so you can copy and paste it straight into your markdown notes.

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
