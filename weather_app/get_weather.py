import os
from pathlib import Path
from dotenv import load_dotenv
import requests

# Load environment variables from the .env file located next to this module.
# This lets us keep the API key out of source control.
base_dir = Path(__file__).resolve().parent
load_dotenv(base_dir / ".env")

# Read the OpenWeatherMap API key from the environment.
api_key = os.getenv("OPENWEATHER_API_KEY")
if not api_key:
    raise RuntimeError("Set OPENWEATHER_API_KEY in your environment")

# Request current weather data for the given location.
# The API returns JSON, which we pass back to the caller.
def get_weather(location):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: Unable to fetch weather data for {location}. Status code: {response.status_code}")
        return None