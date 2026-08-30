# Weather CLI

A simple command-line tool that fetches and displays current weather for any city, using the free Open-Meteo API.

## Features

- Look up weather by city name (converted to coordinates via Open-Meteo's Geocoding API)
- Displays current temperature, wind speed, and a readable condition (e.g. "Partly cloudy")
- Saves each search to a local `history.json` file
- Handles errors gracefully — invalid city names, network issues, and unexpected API responses

## How to Run

1. Install the required library:

pip install requests


2. Run the script:

python weather.py


3. Enter a city name when prompted.

## Example

Enter a city name: Bengaluru

Weather in Bengaluru
Condition: Overcast
Temperature: 22.9°C
Wind speed: 12.4 km/h


## Tech Used

- Python
- [Open-Meteo API](https://open-meteo.com/) (free, no API key required)
- `requests` library

## About

Built as part of a 180-day AI/ML engineering roadmap — Month 1 milestone project focused on API integration, JSON handling, and error handling.
