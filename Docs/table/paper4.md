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