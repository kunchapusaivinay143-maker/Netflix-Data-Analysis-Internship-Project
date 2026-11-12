import pandas as pd

# 1. Import dataset
df = pd.read_csv("Dataset (1).csv")

# 2. Clean whitespace and handle blank values
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].astype("string").str.strip()

df = df.replace(r"^\\s*$", pd.NA, regex=True)
text_fields = ["type", "title", "director", "country", "rating", "duration", "listed_in"]
for col in text_fields:
    df[col] = df[col].fillna("Not Given")

# 3. Remove duplicate records
df = df.drop_duplicates()
df = df.drop_duplicates(subset=["show_id"], keep="first")

# 4. Standardize categorical columns
df["type"] = df["type"].str.casefold().map(
    {"movie": "Movie", "tv show": "TV Show"}
).fillna(df["type"])

df["country"] = df["country"].apply(
    lambda x: ", ".join(part.strip() for part in x.split(","))
    if x != "Not Given" else x
)
df["rating"] = df["rating"].apply(
    lambda x: x.upper().strip() if x != "Not Given" else x
)

# Standardize date format
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
df["date_added"] = df["date_added"].dt.strftime("%Y-%m-%d").fillna("Not Given")

# Ensure release year is numeric
df["release_year"] = pd.to_numeric(df["release_year"], errors="coerce").astype("Int64")

# 5. Export cleaned dataset
df.to_csv("netflix_cleaned.csv", index=False, encoding="utf-8-sig")
print("Cleaned dataset exported successfully!")
print("Rows:", len(df), "| Columns:", len(df.columns))
