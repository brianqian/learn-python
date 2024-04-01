import os
import requests
import json
import time
import asyncio
from dotenv import load_dotenv
from operator import itemgetter

load_dotenv()

asyncio

weather_api_key = os.environ.get("WEATHER_API_KEY")
weather_base_url = "https://api.tomorrow.io/v4/weather/forecast"

ip_addr_url = "http://ip-api.com/json/"


async def get_location():
    res = requests.get(ip_addr_url)
    data = res.json()
    zip, lat, lon = itemgetter("zip", "lat", "lon")(data)
    time.sleep(3)
    return {"lat": float(lat), "lon": float(lon), "zip": int(zip)}


async def get_weather(lat: float, lon: float):
    weather_url = f"{weather_base_url}?location={lat},{lon}&apikey={weather_api_key}"
    forecast = json.loads(requests.get(weather_url).text)

    print(json.dumps(forecast, indent=2))


async def main():
    loc = await get_location()
    weather = await get_weather(loc["lat"], loc["lon"])
    return weather


main()
