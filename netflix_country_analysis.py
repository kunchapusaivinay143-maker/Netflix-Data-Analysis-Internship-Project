import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("netflix_cleaned.csv")

# Clean and split country values
countries = df[["show_id", "type", "country"]].copy()
countries["country"] = countries["country"].fillna("Not Given").astype(str).str.strip()
countries = countries[~countries["country"].isin(["", "Not Given", "nan", "None"])]
countries["country"] = countries["country"].str.split(",")
countries = countries.explode("country")
countries["country"] = countries["country"].astype(str).str.strip()
countries = countries[countries["country"] != ""]
countries = countries.drop_duplicates(["show_id", "country"])

# Count titles by country
counts = countries.groupby("country")["show_id"].nunique().sort_values(ascending=False)
top10 = counts.head(10)
print(top10)

# Top-country ranking chart
top10.sort_values().plot(kind="barh", figsize=(10, 6), title="Top 10 Countries by Netflix Titles")
plt.xlabel("Number of Titles")
plt.tight_layout()
plt.show()

# Movie vs TV Show breakdown
top_rows = countries[countries["country"].isin(top10.index)]
pivot = pd.crosstab(top_rows["country"], top_rows["type"]).reindex(top10.index)
pivot.plot(kind="barh", stacked=True, figsize=(10, 6),
           title="Movies and TV Shows Across Top 10 Countries")
plt.xlabel("Number of Titles")
plt.tight_layout()
plt.show()

# Export complete ranking
ranking = counts.rename("title_count").reset_index()
ranking.columns = ["country", "title_count"]
ranking.insert(0, "rank", range(1, len(ranking) + 1))
ranking.to_csv("netflix_country_ranking.csv", index=False)
