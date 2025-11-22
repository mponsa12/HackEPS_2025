import requests
import json

query = """
    [out:json][timeout:25];
    area["name"="Los Angeles"]->.searchArea;
    // gather results
    relation["boundary"="administrative"](area.searchArea);
    // print results
    out geom;
"""

url = "https://overpass-api.de/api/interpreter"
response = requests.post(url, data={'data': query})

try:
    result = response.json()
    print(json.dumps(result, indent=2))
except Exception as e:
    print("Error decoding JSON response:", e)
    print("Raw response text:")
    print(response.text)
# OUt to out.json 
with open("out.json", "w") as f:
    json.dump(result, f, indent=2)
print("Data written to out.json")