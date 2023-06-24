import requests
from flask import Flask, render_template, request

app = Flask(__name__)

def get_weather(api_key, city):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    data = response.json()

    if "error" in data:
        return None
    else:
        temperature = data["current"]["temp_c"]
        description = data["current"]["condition"]["text"]
        return {"temperature": temperature, "description": description}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city = request.form.get("city")
        api_key = "ae2fa0e696154eb699092948232106"  # Replace with your WeatherAPI.com API key
        weather_data = get_weather(api_key, city)
        if weather_data is not None:
            temperature = weather_data["temperature"]
            description = weather_data["description"]
            return render_template("index.html", temperature=temperature, description=description)
        else:
            error_message = "Failed to fetch weather data. Please try again."
            return render_template("index.html", error=error_message)
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
