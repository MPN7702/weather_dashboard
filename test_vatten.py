import requests
import re

url = "https://fangstrapport.se/sjö/övre-fryken/vattentemperatur"

html = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
).text

match = re.search(
    r'just nu omkring.*?([0-9]+,[0-9]+)\s*°C',
    html,
    re.DOTALL
)

if match:
    print(match.group(1))
