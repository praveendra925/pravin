import pandas as pd

# Load your CSV file
df = pd.read_csv(r"C:\Users\PRAVEENDRA\OneDrive\Documents\save.csv")


# 1. General summary statistics (mean, std, min, max, quartiles)
print("=== Summary Statistics ===")
print(df.describe())

# 2. Median for numeric columns
print("\n=== Median Values ===")
print(df.median(numeric_only=True))

# 3. Standard deviation (if you want separately)
print("\n=== Standard Deviation ===")
print(df.std(numeric_only=True))

# 4. Null value count per column
print("\n=== Null Value Count ===")
print(df.isnull().sum())
