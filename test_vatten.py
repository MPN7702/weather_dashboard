import requests
import re

url = "https://sv.seatemperature.net/sjoar/water-temp-in-mellanfryken"

html = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=10
).text

match = re.search(
    r'Vattentemperatur i sjön Mellan-fryken är i dag ([0-9.]+)°C',
    html
)

if match:
    temp = float(match.group(1))
    print("Temperatur:", temp)
else:
    print("Kunde inte hitta temperatur")
