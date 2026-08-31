import requests
import re

url = "https://fangstrapport.se/sjö/övre-fryken/vattentemperatur"

html = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=20
).text

match = re.search(r'(\d+,\d+)', html)

if match:
    temperatur = float(match.group(1).replace(",", "."))
    print("Övre Fryken:", temperatur)
else:
    print("Ingen temperatur hittades")
