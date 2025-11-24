# Task 4: Logistic Regression Classification

## 📌 Objective

Build a **binary classification model** using **Logistic Regression**, evaluate it with multiple metrics, and understand the sigmoid function and threshold tuning.

---

## 📊 Dataset

You may use:

* **Breast Cancer Wisconsin Dataset** (built-in in scikit‑learn), or
* Your uploaded file: `/mnt/data/data.csv`

---

## 🛠 Tools Used

* Python
* Pandas
* Scikit-learn
* Matplotlib

---

## 🚀 Steps to Follow

### **1. Load Dataset**

Choose any binary classification dataset.

### **2. Train/Test Split**

Split the dataset (typically 80/20) with `train_test_split`.

### **3. Standardization**

Use `StandardScaler` to scale features.

### **4. Model Training**

Train model using:

```
LogisticRegression(max_iter=500)
```

### **5. Predictions**

Generate:

* Class predictions
* Probability predictions

### **6. Evaluation Metrics**

Compute:

* Confusion Matrix
* Precision, Recall, F1‑score
* ROC Curve & AUC
* Threshold tuning

### **7. Threshold Tuning**

Modify default threshold (0.5) based on business requirements.

---

## 📘 What You’ll Learn

* Binary classification pipeline
* Sigmoid function working
* ROC‑AUC curve interpretation
* Confusion matrix analysis
* Impact of threshold on precision & recall

---

## ❓ Interview Questions & Answers

### **1. How does logistic regression differ from linear regression?**

* Linear regression predicts continuous values.
* Logistic regression predicts probabilities for classification.

### **2. What is the sigmoid function?**

Maps any real value to **0–1** probability.

### **3. What is precision vs recall?**

* Precision: Accuracy of positive predictions.
* Recall: Ability to capture actual positives.

### **4. What is the ROC‑AUC curve?**

A plot of TPR vs FPR; AUC shows model’s performance.

### **5. What is the confusion matrix?**

A 2×2 table showing TP, FP, TN, FN.

### **6. What happens if classes are imbalanced?**

Accuracy becomes misleading; consider class weights or resampling.

### **7. How do you choose the threshold?**

Based on business need—recall or precision.

### **8. Can logistic regression be used for multi-class?**

Yes—OvR or multinomial logistic regression.

---

## 📂 Folder Structure (Suggested)

```
Task4_Logistic_Regression/
│-- data.csv
│-- logistic_regression.ipynb
│-- README.md
```

---

## ✔️ Need the full project code, notebook, or PDF report?

Just ask: **"Create Task 4 report"**.
