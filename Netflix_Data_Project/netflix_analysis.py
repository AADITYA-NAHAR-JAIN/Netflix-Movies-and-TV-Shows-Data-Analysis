import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("netflix_titles.csv")

# Show first 5 rows
print(df.head())

# Movies vs TV Shows
type_counts = df['type'].value_counts()

plt.bar(type_counts.index, type_counts.values)
plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()