
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv(r"C:\Users\PRAVEENDRA\OneDrive\Attachments\Desktop\indra.csv")  

numeric_cols = df.select_dtypes(include='number').columns.tolist()


plt.figure(figsize=(10, 8))
corr_matrix = df[numeric_cols].corr()

sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", square=True)
plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()

selected_features = numeric_cols[:5]  
sns.pairplot(df[selected_features], diag_kind='kde')
plt.suptitle("Pairplot of Selected Features", y=1.02)
plt.tight_layout()
plt.show()
