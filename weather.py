import requests

# Your API key
API_KEY = "your_api_key_here"

# Ask user for city name
city = input("Enter city name: ")

# API URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url)
    data = response.json()

    if data["cod"] != 200:
        print("❌ City not found. Please check the name.")
    else:
        # Extract weather details
        city_name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        description = data["weather"][0]["description"]

        print("\n🌍 Weather Details")
        print("----------------------")
        print(f"City: {city_name}, {country}")
        print(f"Temperature: {temp} °C")
        print(f"Weather: {description}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind} m/s")

except Exception as e:
    print("⚠️ Error:", e)
