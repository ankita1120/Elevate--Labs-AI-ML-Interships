Titanic Dataset – Data Cleaning & Preprocessing Project
📌 Project Overview

This project demonstrates the complete data cleaning and preprocessing workflow on the Titanic dataset.
The goal is to prepare raw data for machine learning by handling missing values, encoding categorical features, removing outliers, and scaling numerical columns.

📂 Dataset

The dataset used in this project: Titanic-Dataset.csv

Typical features include:

PassengerId

Survived

Pclass

Name

Sex

Age

SibSp

Parch

Ticket

Fare

Cabin

Embarked

🛠 Tools & Libraries

Python

Pandas

NumPy

Matplotlib

Seaborn

Scikit-Learn

🧭 Steps Performed
1️⃣ Importing & Exploring the Dataset

Loaded the CSV file using Pandas

Checked data structure, data types, and summary statistics

Identified missing values

2️⃣ Handling Missing Data

Filled missing Age values using median

Filled missing Embarked values using mode

Dropped Cabin due to too many nulls

3️⃣ Encoding Categorical Features

Converted Sex column using Label Encoding

Converted Embarked using One-Hot Encoding

4️⃣ Outlier Detection & Removal

Used boxplots and IQR method to remove outliers from:

Age

Fare

5️⃣ Scaling Numerical Features

Applied MinMaxScaler to:

Age

Fare

SibSp

Parch

6️⃣ Saving Cleaned Dataset

Final cleaned dataset was saved as:
📁 Titanic_Cleaned.csv

📊 Key Concepts Learned
✔ Types of Missing Data

MCAR – Missing Completely at Random

MAR – Missing at Random

MNAR – Missing Not at Random

✔ Encoding Techniques

Label Encoding (Ordinal or binary categories)

One-Hot Encoding (Nominal categories)

✔ Scaling

Normalization (MinMaxScaler) – scales between 0 and 1

Standardization – mean 0, std 1 (not used here but explained)

✔ Outlier Detection

Boxplots

IQR method

✔ Importance of Preprocessing

Good preprocessing improves:

Model accuracy

Data quality

Training stability

📁 Project Files
File	Description
Titanic-Dataset.csv	Raw dataset
Titanic_Cleaned.csv	Cleaned & processed dataset
notebook.ipynb	(optional) Full code implementation
README.md	Project documentation
🚀 How to Run

Clone the repository

Install dependencies

pip install pandas numpy matplotlib seaborn scikit-learn


Run the notebook or Python script

Cleaned data will be saved automatically

📌 Future Enhancements

Add full EDA (visualizations & insights)

Build ML models (Logistic Regression / Random Forest)

Deploy using Streamlit or Flask