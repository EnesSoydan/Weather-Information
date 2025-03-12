import requests
import os

API_KEY = os.getenv("API_KEY")
CITY=input("Which city do you want to learn weather information? ")
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response=requests.get(URL)
if response.status_code == 200:
	data = response.json()
	temperature = data["main"]["temp"]
	weather = data["weather"][0]["description"]

	print(f"Weather information for {CITY}:  ")
	print(f"Temperature: {temperature}°C")
	print(f"Weather: {weather}")
else:
	print("Couldn't get data from API,Check your API Key or connection!")