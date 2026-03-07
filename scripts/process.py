import os
import json
import requests

BASE_URL = "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_10m_admin_1_states_provinces.geojson"
DATA_DIR = "data"


def download_geojson():
    try:
        os.makedirs(DATA_DIR, exist_ok=True)

        response = requests.get(BASE_URL)
        response.raise_for_status()
        geojson_data = response.json()
        geojson_data.pop("crs", None)

        with open(f"{DATA_DIR}/admin1.geojson", "w", encoding="utf-8") as f:
            json.dump(geojson_data, f, ensure_ascii=False)
        print("Download complete: admin1.geojson")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    download_geojson()
