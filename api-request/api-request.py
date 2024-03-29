import json
import os
import webbrowser
import requests

weather_api_key = os.environ.get("WEATHER_API_KEY")
weather_url = "https://api.tomorrow.io/v4/weather/"

ip_addr_url = "http://ip-api.com/json/"


def make_request():
    res = requests.get()
    pass
