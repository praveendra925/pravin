import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"C:\Users\PRAVEENDRA\OneDrive\Attachments\Desktop\trends.csv")  # Replace with your file

# Basic info
print("\n--- Dataset Info ---")
print(df.info())

# Summary statistics
print("\n--- Summary Statistics ---")
print(df.describe())

# Check for missing values
print("\n--- Missing Values ---")
print(df.isnull().sum())

# Correlation heatmap (to identify trends and relationships)
plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()

# Pairplot for relationships (small datasets only)
# sns.pairplot(df.select_dtypes(include='number'))
# plt.show()

# Boxplots for outlier detection
numeric_cols = df.select_dtypes(include='number').columns
for col in numeric_cols:
    plt.figure(figsize=(8, 4))
    sns.boxplot(x=df[col], color='lightgreen')
    plt.title(f'Boxplot of {col} (Outlier Detection)')
    plt.tight_layout()
    plt.show()

# Histograms to view distributions
for col in numeric_cols:
    plt.figure(figsize=(8, 4))
    sns.histplot(df[col], kde=True, color='cornflowerblue')
    plt.title(f'Distribution of {col}')
    plt.tight_layout()
    plt.show()
