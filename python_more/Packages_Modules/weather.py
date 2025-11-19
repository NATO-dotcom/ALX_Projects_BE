# weather.py

import requests

API_KEY = "YOUR_API_KEY_HERE"
CITY = "Nairobi"

url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    temperature = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"Weather in {CITY}:")
    print("Temperature:", temperature, "°C")
    print("Condition:", condition)

else:
    print("Failed to fetch weather data:", response.status_code)
# This script fetches and displays the current weather information for a specified city using a weather API.