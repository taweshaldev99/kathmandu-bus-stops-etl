import pandas as pd

# Load raw data
df = pd.read_csv("osm_bus_stops.csv")

print("🔹 Raw data shape:", df.shape)

# 1. Drop duplicates by ID or (lat, lon)
df = df.drop_duplicates(subset=["id"])
df = df.drop_duplicates(subset=["lat", "lon"])

# 2. Handle missing names
df["name"] = df["name"].fillna("Unknown Stop")
df.loc[df["name"].str.strip() == "", "name"] = "Unknown Stop"

# 3. Standardize text fields
df["name"] = df["name"].str.title()       # e.g. "ratna park" → "Ratna Park"
df["operator"] = df["operator"].fillna("").str.title()

# 4. Keep only important columns
clean_df = df[["id", "name", "lat", "lon", "operator"]]

# 5. Save cleaned dataset
clean_df.to_csv("osm_bus_stops_clean.csv", index=False)

print("✅ Cleaned data saved: osm_bus_stops_clean.csv")
print("🔹 Cleaned data shape:", clean_df.shape)
print(clean_df.head())
