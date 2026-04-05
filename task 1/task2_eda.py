import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set_style("darkgrid")

df = pd.read_csv("data/titanic.csv")

print("First rows:")
print(df.head())

print("\nInfo:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

os.makedirs("../output", exist_ok=True)

# Survival count
sns.countplot(x='Survived', data=df)
plt.title("Survival Count")
plt.show()
plt.savefig("../output/survival.png")
plt.close()

# Gender vs Survival
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title("Gender vs Survival")
plt.show()
plt.savefig("../output/gender_survival.png")
plt.close()

# Age distribution
sns.histplot(df['Age'], bins=10, kde=True)
plt.title("Age Distribution")
plt.show()
plt.savefig("../output/age_dist.png")
plt.close()

# Correlation heatmap
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.title("Correlation Heatmap")
plt.show()
plt.savefig("../output/heatmap.png")
plt.close()

print("EDA Completed!")

