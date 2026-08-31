import requests
import re

url = "https://sv.seatemperature.net/sjoar/water-temp-in-mellanfryken"

html = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=10
).text

match = re.search(
    r'<div class="temp-value">([0-9.]+)<span>°C</span>',
    html
)

if match:
    print("Temperatur:", match.group(1))
else:
    print("Kunde inte hitta temperatur")
