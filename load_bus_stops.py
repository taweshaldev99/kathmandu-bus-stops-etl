import pandas as pd
import sqlite3

# 1. Load the cleaned CSV
df = pd.read_csv("osm_bus_stops_clean.csv")

# 2. Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect("transport.db")
cursor = conn.cursor()

# 3. Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS bus_stops (
    id INTEGER PRIMARY KEY,
    name TEXT,
    lat REAL,
    lon REAL,
    operator TEXT
)
""")

# 4. Insert data into table
df.to_sql("bus_stops", conn, if_exists="replace", index=False)

conn.commit()
conn.close()

print("✅ Data loaded into SQLite database: transport.db")
