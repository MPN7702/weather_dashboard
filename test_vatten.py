import requests

url = "https://fangstrapport.se/sjö/övre-fryken/vattentemperatur"

response = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=20
)

print("Status:", response.status_code)
print(response.url)
print(response.text[:3000])
