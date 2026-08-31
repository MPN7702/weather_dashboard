import requests

url = "https://sv.seatemperature.net/sjoar/water-temp-in-mellanfryken"

html = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=10
).text

print("HTML LÄNGD:", len(html))
print(html[:1000])
