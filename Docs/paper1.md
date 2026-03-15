stripped-down breakdown of the first paper, formatted exactly how you asked. You can copy and paste this straight into your markdown notes. It has all the technical meat without any of the academic fluff.

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

