from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(City="Kansas City"):
    request_url = f'http://api.openweathermap.org/2.5/weather?app_id={os.getenv("API_KEY")}&q={City}&units=imperial'

    weather_data = requests.get(request_url).json()

    return weather_data

if __name__ == "__main__":
    print('\n*** Get Weather Conditions **\n')
    city = input("\nPlease enter city name: ")
    weather_data = get_current_weather(city)
    print('\n')
    pprint(weather_data)
