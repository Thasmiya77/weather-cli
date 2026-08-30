import requests
import json
import os

WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    71: "Slight snow",
    73: "Moderate snow",
    75: "Heavy snow",
    80: "Slight rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    95: "Thunderstorm",
}

def get_coordinates(city_name):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city_name}
    response = requests.get(url, params=params)
    data = response.json()

    if "results" not in data:
        return None

    first_result = data["results"][0]
    lat = first_result["latitude"]
    lon = first_result["longitude"]
    return lat, lon


def get_weather(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {"latitude": lat, "longitude": lon, "current_weather": True}
    response = requests.get(url, params=params)
    data = response.json()
    return data


def format_weather(city_name, weather_data):
    current = weather_data["current_weather"]
    temp = current["temperature"]
    wind = current["windspeed"]
    code = current["weathercode"]
    description = WEATHER_CODES.get(code, "Unknown conditions")

    print(f"\nWeather in {city_name}")
    print(f"Condition: {description}")
    print(f"Temperature: {temp}°C")
    print(f"Wind speed: {wind} km/h")


def save_to_history(city_name, weather_data):
    history_file = "history.json"

    if os.path.exists(history_file):
        with open(history_file, "r") as f:
            history = json.load(f)
    else:
        history = []

    current = weather_data["current_weather"]
    entry = {
        "city": city_name,
        "temperature": current["temperature"],
        "time": current["time"],
    }
    history.append(entry)

    with open(history_file, "w") as f:
        json.dump(history, f, indent=2)


def main():
    city_name = input("Enter a city name: ")

    try:
        coordinates = get_coordinates(city_name)
        if coordinates is None:
            print("City not found. Please check the spelling and try again.")
            return

        lat, lon = coordinates
        weather_data = get_weather(lat, lon)
        format_weather(city_name, weather_data)
        save_to_history(city_name, weather_data)

    except requests.exceptions.RequestException:
        print("Network error — please check your internet connection.")
    except (KeyError, IndexError):
        print("Unexpected response from the weather service.")


if __name__ == "__main__":
    main()