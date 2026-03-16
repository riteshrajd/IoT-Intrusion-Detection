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