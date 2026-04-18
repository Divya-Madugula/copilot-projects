import requests

api_key = 'e5c5265d728b30478de3b06b1969c5ae'

def get_weather(location):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: Unable to fetch weather data for {location}. Status code: {response.status_code}")
        return None