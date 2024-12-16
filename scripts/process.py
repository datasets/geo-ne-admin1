import os
import requests

BASE_URL = 'https://github.com/wmgeolab/geoBoundaries/raw/main/releaseData/CGAZ/geoBoundariesCGAZ_ADM1.geojson'
DATA_DIR = 'data'

def download_geojson():
    try:
        os.makedirs(DATA_DIR, exist_ok=True)

        response = requests.get(BASE_URL)
        response.raise_for_status()
        geojson_data = response.content

        with open(f'{DATA_DIR}/admin1.geojson', 'wb') as f:
            f.write(geojson_data)
        print("Download complete: admin1.geojson")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    download_geojson()
