import requests

from dotenv import load_dotenv
import os

load_dotenv()

# get api key
api_key = os.environ.get("WEATHER_API_KEY")

# define function to get weather data
def get_current_weather_C(city):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    data = response.json()
    print(data)
    return f"the current temperature in {city} is {data['current']['temp_c']} degrees celsius"

def get_current_weather_F(city):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    data = response.json()
    print(data)
    return f"the current temperature in {city} is {data['current']['temp_f']} fahrenheit degrees"