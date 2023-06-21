import requests
import json

def get_weather(api_key, city):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    data = json.loads(response.text)

    if "error" in data:
        print("Failed to fetch weather data.")
    else:
        temperature = data["current"]["temp_c"]
        description = data["current"]["condition"]["text"]
        print(f"Temperature: {temperature}°C")
        print(f"Description: {description}")

def main():
    api_key = "ae2fa0e696154eb699092948232106"  # Replace with your WeatherAPI.com API key
    city = input("Enter city name: ")
    get_weather(api_key, city)

if __name__ == "__main__":
    main()
