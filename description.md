Here is your complete **Master Document**. It is divided into two parts: the **Official Proposal** (to show the professor) and the **Internal Strategy Notes** (for your team's reference).

---

### **PART 1: OFFICIAL PROJECT PROPOSAL (For Professor)**

**Project Title:** Fed-IoT: Lightweight Federated Ensemble for Heterogeneous Intrusion Detection

**1. Problem Statement**
Current IoT security solutions rely on centralized Deep Learning, which fails in two critical engineering areas:

* **Device Heterogeneity (The "Non-IID" Problem):** A single global model cannot generalize across diverse devices (e.g., Cameras vs. Thermostats). Averaging their divergent traffic patterns (standard Federated Averaging) dilutes the model's accuracy for specific device types.
* **Resource Constraints:** IoT devices lack the RAM and battery to run heavy Artificial Neural Networks (ANNs).

**2. Proposed Solutions**

* **Issue:** **Device Heterogeneity**
* **Solution:** **Federated Ensemble Architecture.**
* **Details:** We propose a **Dual-Model** approach. Each device maintains two models:
1. A **Global Model** (trained across all nodes) to detect general threats like DDoS.
2. A **Category-Specific Model** (trained only on similar devices, e.g., "Camera Cluster") to detect unique local anomalies.


* **Outcome:** The device aggregates outputs from both models, ensuring robust detection for both global botnets and device-specific exploits.


* **Issue:** **Resource Constraints**
* **Solution:** **Lightweight Support Vector Machines (SVMs).**
* **Details:** Running two models is computationally expensive. To solve this, we replace standard Neural Networks with **SVMs**.
* **Research Basis:** Recent studies (Al-Faqih et al.) demonstrate that SVMs achieve comparable accuracy (~97%) to ANNs but with significantly lower latency (milliseconds vs. seconds), allowing us to run the ensemble within a standard IoT power budget.



**3. Implementation Roadmap**

* **Tech Stack:** Python, **Flower (`flwr`) Framework** for the federated loop, Scikit-Learn for SVMs.
* **Dataset:** **NSL-KDD** (Partitioned into non-IID chunks to simulate heterogeneous traffic).
* **Deliverable:** A simulation of 3 distinct clients (heterogeneous nodes) successfully collaborating to detect attacks without sharing raw data.

---

### **PART 2: INTERNAL STRATEGY & EXTRAS (For Team Reference)**

**1. The "Backup" Plan: Personalization (Fine-Tuning)**

* **Trigger:** If building the "Dual-Model Ensemble" becomes too hard to code or too heavy for the simulation.
* **The Pivot:** Switch to **Global + Fine-Tuning**.
* **How:** The device downloads the Global Model and runs 1-2 extra training epochs on its *local data* before using it.
* **The Pitch to Prof:** "We optimized the Ensemble approach. Instead of maintaining two separate models, we found it more efficient to have a single Global backbone that 'adapts' to the device via local fine-tuning."



**2. Ensemble Logic (How to code the main idea)**

* **Training:** Train *both* the Global and Category models on *all* new local data. Do not try to filter "which data goes where."
* **Inference:** Run the traffic through both models. Average their prediction scores (e.g., `(Score_Global + Score_Category) / 2`). If the average > threshold, trigger an alert.
* **No "Decision Model":** Do not build a third model to decide which one to trust. It adds unnecessary complexity.

**3. Data Handling (Simulating Heterogeneity)**

* **The Trick:** Manually split the NSL-KDD dataset.
* **Client 1 (Camera):** Give it mostly `DoS` attacks.
* **Client 2 (Thermostat):** Give it mostly `Probe` attacks.
* **Client 3 (Fridge):** Give it a mix of normal traffic and `R2L` attacks.


* **Why:** This forces the "Global" model to learn everything, while the "Category" models become experts in their specific attack types.

**4. Why we chose SVM (Research Backing)**

* **Key Stat:** SVM training time was **27s** vs. ANN's **41s**.
* **Key Stat:** SVM accuracy was **~97-98%**, comparable to Deep Learning.
* **Use these stats** if the professor questions why we aren't using "modern" Deep Learning.