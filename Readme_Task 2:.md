Exploratory Data Analysis (EDA)
🎯 Objective

To understand the dataset using descriptive statistics and visualizations, and to identify important patterns that will guide further preprocessing and modeling.

🛠 Tools Used

Pandas – Data handling

Matplotlib – Charts

Seaborn – Visualizations

Plotly – Interactive visuals

📝 Mini EDA Guide
1️⃣ Generate Summary Statistics

Mean, median, standard deviation

Missing values

Unique value counts

df.describe()
df.isnull().sum()
df.nunique()

2️⃣ Visualize Numeric Features

Use histograms, KDE plots, and boxplots.

sns.histplot(df['Age'], kde=True)
plt.show()

sns.boxplot(x=df['Fare'])
plt.show()

3️⃣ Analyze Feature Relationships

Pairplots and correlation matrix help reveal relationships.

sns.pairplot(df[['Age', 'Fare', 'Survived']])
plt.show()


For correlation:

numeric_df = df.select_dtypes(include='number')

sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.show()

4️⃣ Identify Patterns, Trends, Anomalies

Examples from Titanic dataset:

Younger passengers had higher survival rates.

Females survived more than males.

Higher ticket fare ↗ increased survival (first-class passengers).

Many missing values in Age and Cabin.

5️⃣ Make Feature-Level Inferences

These insights help in:

Feature engineering

Handling skewness

Detecting outliers

Improving model performance

📚 What You'll Learn

Descriptive statistics

Visual analysis

Outlier detection

Correlation patterns

Data-driven decision-making

💼 Interview Questions & Sample Answers
1️⃣ What is the purpose of EDA?

To understand the structure, distribution, and quality of data before building ML models.

2️⃣ How do boxplots help in understanding a dataset?

They show the distribution, median, quartiles, and outliers.

3️⃣ What is correlation and why is it useful?

Correlation measures how strongly two numeric variables move together.
Helps detect relationships, multicollinearity, and feature importance.

4️⃣ How do you detect skewness in data?

Visually using histograms

Using df.skew()
Right-skew → long right tail
Left-skew → long left tail

5️⃣ What is multicollinearity?

When two or more features are highly correlated, causing redundancy and unstable model coefficients.

6️⃣ What tools do you use for EDA?

Pandas, Matplotlib, Seaborn, Plotly, Jupyter Notebook.

7️⃣ Can you explain a time when EDA helped you find a problem?

(You can reuse this answer)

During a churn prediction project, EDA revealed missing tenure values for customers in one region. This indicated a data pipeline issue, which we fixed. This improved model accuracy significantly.

8️⃣ What is the role of visualization in ML?

Visualizations reveal patterns, help detect outliers, improve understanding, and guide better feature engineering.