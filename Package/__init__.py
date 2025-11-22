import requests

if __name__ == "__main__":
    url = "https://api.census.gov/data/2023/geoinfo"
    data = requests.get(url).json()
    print(data)