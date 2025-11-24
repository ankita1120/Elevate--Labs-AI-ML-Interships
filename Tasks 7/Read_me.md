SVM Classification Project

This project demonstrates how to use Support Vector Machines (SVMs) for both linear and non-linear binary classification using Scikit-learn, NumPy, and Matplotlib.

📌 Overview

Load and prepare a dataset for binary classification

Train SVM models using Linear and RBF kernels

Visualize decision boundaries in 2D

Tune hyperparameters (C, gamma) using Grid Search + Cross Validation

Evaluate model performance

📂 Dataset

The dataset is loaded from data.csv and includes:

Two selected numerical features: radius_mean and texture_mean

Target labels: diagnosis (encoded as 0/1)

⚙️ Installation
pip install numpy pandas matplotlib scikit-learn

▶️ Running the Code

Run the Python script or notebook containing the SVM workflow.
The code includes:

Data loading and preprocessing

SVM training

Hyperparameter tuning

Decision boundary visualization

📊 Features
1. Linear SVM

Finds a straight-line (or hyperplane) separator

Works best when data is linearly separable

2. RBF Kernel SVM

Handles non-linear decision boundaries

Uses Gaussian similarity to map data to high-dimensional space

🔧 Hyperparameters
C Parameter

Controls margin-softness:

High C → less misclassification → risk of overfitting

Low C → more misclassification allowed → better generalization

Gamma (γ)

Only for RBF kernel:

High gamma → tighter, more complex boundaries

Low gamma → smoother, simpler boundaries

🔍 Model Evaluation

The project evaluates:

Training accuracy

Test accuracy

Best hyperparameters via Grid Search

Visual comparison of decision boundaries

📦 Output

Figures include:

Linear SVM decision boundary

RBF SVM decision boundary

Optimized RBF decision boundary after tuning

📘 Interview Questions Included

Support vectors

Kernel types

Difference between linear and RBF

Soft margin concept

Overfitting in SVM

Regression with SVR

📁 Project Structure
project/
├── data.csv
├── svm_classification.py    # main script (example)
├── readme.md
└── outputs/
    ├── linear_decision_boundary.png
    ├── rbf_decision_boundary.png
    └── best_rbf_decision_boundary.png

▶️ Usage

Place data.csv in the project directory.

Run the main script:

python svm_classification.py


Outputs (plots + printed metrics) will appear on screen or in the outputs/ folder.




Linear SVM boundary

RBF SVM boundary

Grid Search optimized boundary

(Add images here once generated.)

📚 References

Scikit-learn Documentation

SVM Theory (Cortes & Vapnik, 1995)

Kernel Methods Tutorial