import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset (replace with your actual file path)
data = pd.read_csv(r"C:\Users\PRAVEENDRA\OneDrive\Attachments\Desktop\indra.csv")  # or use pd.read_excel("your_file.xlsx")

# Select numeric columns only
numeric_cols = data.select_dtypes(include='number')

# Histograms for numeric features
for column in numeric_cols.columns:
    plt.figure(figsize=(8, 4))
    plt.hist(data[column].dropna(), bins=30, color='skyblue', edgecolor='black')
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Boxplots for numeric features
for column in numeric_cols.columns:
    plt.figure(figsize=(8, 4))
    sns.boxplot(x=data[column], color='orange')
    plt.title(f'Boxplot of {column}')
    plt.xlabel(column)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
