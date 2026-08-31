import requests

url = "https://sv.seatemperature.net/sjoar/water-temp-in-mellanfryken"

response = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=20,
    allow_redirects=True
)

print("STATUS:", response.status_code)
print("URL:", response.url)
print("HTML LÄNGD:", len(response.text))

print("\nFÖRSTA 1000 TECKNEN:\n")
print(response.text[:1000])
