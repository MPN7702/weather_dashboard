import requests

url = "https://fangstrapport.se/sjö/övre-fryken/vattentemperatur"

html = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=20
).text

for line in html.splitlines():
    if "°C" in line:
        print(line)
