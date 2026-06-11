import requests

API_KEY = "YOUR_API_KEY"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid="API_KEY"&units=metric"

try:
    response = requests.get(url)

    print("\nStatus Code:", response.status_code)
    print("Raw Response:", response.text)

    if response.status_code == 200:
        data = response.json()

        print("\nWeather Information")
        print("-" * 30)
        print("City:", data["name"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Humidity:", data["main"]["humidity"], "%")
        print("Weather:", data["weather"][0]["description"])

    else:
        print("\nAPI Error!")

except Exception as e:
    print("Error:", e)
