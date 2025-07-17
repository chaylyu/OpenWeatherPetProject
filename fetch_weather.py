import requests

api_key = "38ec8b3fc16b83899f2eae2d13edcab4"
base_url = "http://api.openweathermap.org/data/2.5/weather"  # ✅ правильний endpoint

city_name = input("Enter city name: ")

params = {
    "q": city_name,
    "appid": api_key
}

response = requests.get(base_url, params=params)
x = response.json()

if x.get("cod") == 200:
    y = x["main"]
    current_temperature = y["temp"]
    current_pressure = y["pressure"]
    current_humidity = y["humidity"]
    z = x["weather"]
    weather_description = z[0]["description"]

    print("Temperature (in Kelvin) = " + str(current_temperature) +
          "\nPressure (in hPa) = " + str(current_pressure) +
          "\nHumidity (in %) = " + str(current_humidity) +
          "\nDescription = " + str(weather_description))
else:
    print("❌ Error:", x.get("message", "City Not Found"))
