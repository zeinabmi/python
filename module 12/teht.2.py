import requests

api_key = "	e10ece65e6996086bb8ff11f8263e88f"

city = input("Enter city name: ")

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city,
    "appid": api_key
}

response = requests.get(url, params=params)
data = response.json()
print(data)

weather = data["weather"][0]["description"]
temperature = data["main"]["temp"]

celsius = temperature - 273.15

print("Weather:", weather)
print("Temperature:", round(celsius, 1), "C")