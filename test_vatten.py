import requests

url = "https://sv.seatemperature.net/sjoar/water-temp-in-mellanfryken"

html = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=10
).text

print("temp-value =", html.find("temp-value"))
print("Aktuell vattentemperatur =", html.find("Aktuell vattentemperatur"))
print("Vattentemperatur i sjön =", html.find("Vattentemperatur i sjön"))
print("18.5 =", html.find("18.5"))
