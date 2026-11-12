import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load and prepare data
df = pd.read_csv("netflix_cleaned.csv")
df["release_year"] = pd.to_numeric(df["release_year"], errors="coerce")
df = df.dropna(subset=["release_year"])
df["release_year"] = df["release_year"].astype(int)

# Step 2: Count titles by release year
yearly = df.groupby("release_year").size().sort_index()
print("Yearly title counts:")
print(yearly)

# Step 3: Calculate year-on-year growth or decline
trend = yearly.to_frame("title_count")
trend["yoy_change"] = trend["title_count"].diff()
trend["yoy_change_pct"] = trend["title_count"].pct_change() * 100
print("\\nYear-on-year trend:")
print(trend.tail(15))

# Step 4: Visualize yearly trend
plt.figure(figsize=(11, 6))
plt.plot(yearly.index, yearly.values, marker="o")
plt.title("Netflix Titles by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Compare Movies and TV Shows
yearly_type = df.groupby(["release_year", "type"]).size().unstack(fill_value=0)
yearly_type.plot(figsize=(11, 6), marker="o")
plt.title("Yearly Titles by Content Type")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Step 5: Export results
trend.to_csv("netflix_yearly_release_counts.csv")
yearly_type.to_csv("netflix_yearly_release_by_type.csv")
