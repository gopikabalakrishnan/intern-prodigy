import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set_style("darkgrid")

file_path = "../data/API_SP.POP.TOTL_DS2_en_csv_v2_207128.csv"

df = pd.read_csv(file_path, skiprows=4)

year = "2022"
df = df[['Country Name', year]].dropna()
df.rename(columns={year: 'Population'}, inplace=True)

os.makedirs("../output", exist_ok=True)

top10 = df.sort_values(by='Population', ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x='Population', y='Country Name', data=top10)
plt.title("Top 10 Countries by Population (2022)")
plt.tight_layout()
plt.savefig("../output/bar_chart.png")
plt.close()

plt.figure(figsize=(8, 5))
sns.histplot(df['Population'], bins=20, kde=True)
plt.title("Population Distribution (2022)")
plt.tight_layout()
plt.show()
plt.savefig("../output/histogram.png")
plt.close()


print("Done!")
