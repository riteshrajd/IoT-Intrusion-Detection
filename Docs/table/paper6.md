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