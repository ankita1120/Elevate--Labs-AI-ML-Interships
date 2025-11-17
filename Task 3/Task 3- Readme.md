Linear Regression Project
📈 Objective

Implement and understand simple and multiple linear regression using Scikit‑learn, evaluate the model using standard metrics, and visualize results.

🛠 Tools & Libraries

Python

Pandas – Data loading & preprocessing

Scikit‑learn – Linear Regression modeling

Matplotlib / Seaborn – Visualization

📂 Dataset

Use the provided Housing.csv dataset or any numerical dataset containing:

Features (e.g., area, bedrooms, bathrooms)

Target variable (e.g., price)

🚀 Steps to Implement Linear Regression
1️⃣ Load & Explore Dataset

Read CSV file using Pandas

Check null values, data types, summary statistics

2️⃣ Data Preprocessing

Handle missing values

Encode categorical variables (if present)

Select features (X) and target (y)

3️⃣ Train-Test Split

Use train_test_split to divide data for model evaluation.

4️⃣ Train Linear Regression Model

Use LinearRegression() from Scikit‑learn.

5️⃣ Model Evaluation

Evaluate with:

MAE (Mean Absolute Error)

MSE (Mean Squared Error)

RMSE (Root Mean Squared Error)

R² Score (Coefficient of Determination)

6️⃣ Interpret Coefficients

Understand how each feature influences the target.

7️⃣ Visualize Regression Line

For simple linear regression:

Scatter plot

Regression line overlay

📊 What You Will Learn

Regression modeling

Data preprocessing

Evaluation metrics

Coefficient interpretation

Visualization of regression results

📝 Example Code Snippet
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import numpy as np


# Load dataset
df = pd.read_csv("Housing.csv")


# Select features and target
X = df[['area', 'bedrooms', 'bathrooms']]
y = df['price']


# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Model training
model = LinearRegression()
model.fit(X_train, y_train)


# Prediction
y_pred = model.predict(X_test)


# Evaluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)


print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R² Score:", r2)


# Coefficients
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)
📘 Conclusion

This project demonstrates the complete workflow of implementing linear regression, from data preparation to evaluation and visualization. It serves as a strong foundation for understanding predictive modeling.