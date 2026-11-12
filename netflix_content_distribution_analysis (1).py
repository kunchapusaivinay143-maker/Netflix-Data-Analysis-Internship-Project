import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the cleaned dataset
df = pd.read_csv("netflix_cleaned.csv")

# Step 2: Count Movies and TV Shows
content_counts = df["type"].value_counts().reindex(
    ["Movie", "TV Show"], fill_value=0
)
total_titles = content_counts.sum()
content_percentages = content_counts / total_titles * 100

print("Content counts:")
print(content_counts)
print("\\nContent percentages:")
print(content_percentages.round(2))

# Step 3: Bar chart using Matplotlib
plt.figure(figsize=(8, 5))
ax = sns.barplot(
    x=content_counts.index,
    y=content_counts.values
)
ax.set_title("Netflix Content Distribution: Movies vs TV Shows")
ax.set_xlabel("Content Type")
ax.set_ylabel("Number of Titles")
ax.set_ylim(0, max(content_counts.values) * 1.18)
for i, value in enumerate(content_counts.values):
    pct = content_percentages.iloc[i]
    ax.text(i, value, f"{value:,} ({pct:.1f}%)", ha="center", va="bottom")
plt.tight_layout()
plt.savefig("netflix_content_distribution_bar.png", dpi=180)
plt.show()

# Step 4: Pie chart for proportions
plt.figure(figsize=(7, 6))
plt.pie(
    content_counts.values,
    labels=content_counts.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Proportion of Movies and TV Shows on Netflix")
plt.axis("equal")
plt.tight_layout()
plt.savefig("netflix_content_distribution_pie.png", dpi=180)
plt.show()

# Step 5: Key findings
movies = int(content_counts["Movie"])
tv_shows = int(content_counts["TV Show"])
print(f"Total titles: {total_titles:,}")
print(f"Movies: {movies:,} ({content_percentages['Movie']:.2f}%)")
print(f"TV Shows: {tv_shows:,} ({content_percentages['TV Show']:.2f}%)")
print(f"Difference: {movies - tv_shows:,} more Movies")
print(f"Movie-to-TV-Show ratio: {movies / tv_shows:.2f}:1")
