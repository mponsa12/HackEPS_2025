import requests
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

CENSUS_API_KEY = "7490eb0d3645093417597f03064dabcf9afe432f"

# Lista de barrios con un punto aproximado (lat, lon)
barrios = {
    "Koreatown": (34.0595, -118.308),
    "Compton": (33.8958, -118.2201),
    "Skid Row": (34.0407, -118.2468),
    "Bel-Air": (34.083, -118.445),
    "Watts": (33.9455, -118.2478),
    "Hollywood": (34.098, -118.329),
    "Boyle Heights": (34.0456, -118.211),
    "Echo Park": (34.0782, -118.2607),
    "Westlake": (34.0611, -118.2741),
    "Mid City": (34.0266, -118.343),
    "Brentwood": (34.055, -118.445),
    "Pacific Palisades": (34.034, -118.510),
    "Leimert Park": (34.0103, -118.2923),
    "Lincoln Heights": (34.0839, -118.205),
    "Porter Ranch": (34.2547, -118.565)
}

# Descargar shapefile ZCTAs del Censo (2021)
zcta_url = "https://www2.census.gov/geo/tiger/TIGER2021/ZCTA520/tl_2021_us_zcta520.zip"
zcta_gdf = gpd.read_file(zcta_url)
zcta_gdf = zcta_gdf.to_crs("EPSG:4326")

# Variable de población total por ZCTA
VARIABLE = "B01003_001E"

resultados = []

for barrio, (lat, lon) in barrios.items():
    point = Point(lon, lat)
    # Buscar ZCTA que contenga el punto
    zcta_match = zcta_gdf[zcta_gdf.geometry.contains(point)]
    if not zcta_match.empty:
        zcta_code = zcta_match.iloc[0]["ZCTA5CE20"]
        # Consultar población del ZCTA
        url = f"https://api.census.gov/data/2021/acs/acs5?get={VARIABLE}&for=zip%20code%20tabulation%20area:{zcta_code}&key={CENSUS_API_KEY}"
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()[1]
            poblacion = int(data[0])
        else:
            poblacion = None
    else:
        poblacion = None
    
    resultados.append({"barrio": barrio, "poblacion": poblacion})

df = pd.DataFrame(resultados)
print(df)
