import requests, json, pandas as pd

# Kathmandu Valley bounding box (S, W, N, E)
BBOX = (27.60, 85.20, 27.80, 85.45)
OVERPASS_URL = "https://overpass-api.de/api/interpreter"

query = f"""
[out:json][timeout:180];
(
  node["highway"="bus_stop"]({BBOX[0]},{BBOX[1]},{BBOX[2]},{BBOX[3]});
  node["public_transport"="platform"]({BBOX[0]},{BBOX[1]},{BBOX[2]},{BBOX[3]});
);
out body;
"""

resp = requests.post(OVERPASS_URL, data={"data": query})
data = resp.json()

rows = []
for el in data["elements"]:
    tags = el.get("tags", {})
    rows.append({
        "id": el["id"],
        "name": tags.get("name", ""),
        "lat": el["lat"],
        "lon": el["lon"],
        "operator": tags.get("operator", "")
    })

df = pd.DataFrame(rows)
df.to_csv("osm_bus_stops.csv", index=False)
print("✅ Saved bus stops:", len(df))
