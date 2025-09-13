import sqlite3

# Connect to your SQLite DB
conn = sqlite3.connect("transport.db")
cursor = conn.cursor()

print("✅ Connected to transport.db")

# 1. Count total bus stops
cursor.execute("SELECT COUNT(*) FROM bus_stops")
print("Total Bus Stops:", cursor.fetchone()[0])

# 2. Sample 5 bus stops
cursor.execute("SELECT name, lat, lon FROM bus_stops LIMIT 5")
print("\nSample Bus Stops:")
for row in cursor.fetchall():
    print(row)

# 3. Find unnamed bus stops
cursor.execute("SELECT COUNT(*) FROM bus_stops WHERE name = 'Unknown Stop'")
print("\nUnnamed Bus Stops:", cursor.fetchone()[0])

# 4. Top operators (if operator column has data)
cursor.execute("""
SELECT operator, COUNT(*) AS stop_count
FROM bus_stops
WHERE operator <> ''
GROUP BY operator
ORDER BY stop_count DESC
LIMIT 5
""")
print("\nTop Operators:")
for row in cursor.fetchall():
    print(row)

conn.close()
