import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Generate the dataset
np.random.seed(42)
n = 100

data = {
    'age': np.random.randint(22, 60, size=n),
    'salary': np.random.normal(loc=50000, scale=15000, size=n).astype(int),
    'years_of_experience': np.random.normal(loc=10, scale=5, size=n).clip(0),
    'department': np.random.choice(['HR', 'IT', 'Finance', 'Marketing', 'Sales'], size=n)
}

df = pd.DataFrame(data)

# Step 2: Summary statistics
print("Summary Statistics:\n")
print(df.describe())

# Step 3: Histograms
df.hist(figsize=(10, 6), bins=20, edgecolor='black')
plt.suptitle('Histograms of Numeric Features')
plt.tight_layout()
plt.show()

# Step 4: Boxplots
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
sns.boxplot(x=df['age'])
plt.title('Boxplot - Age')

plt.subplot(1, 3, 2)
sns.boxplot(x=df['salary'])
plt.title('Boxplot - Salary')

plt.subplot(1, 3, 3)
sns.boxplot(x=df['years_of_experience'])
plt.title('Boxplot - Years of Experience')

plt.tight_layout()
plt.show()

# Step 5: Correlation heatmap
plt.figure(figsize=(8, 6))
corr = df[['age', 'salary', 'years_of_experience']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()

# Step 6: Pairplot
sns.pairplot(df[['age', 'salary', 'years_of_experience']])
plt.suptitle('Pairplot of Numeric Features', y=1.02)
plt.show()
