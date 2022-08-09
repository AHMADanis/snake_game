import requests
from twilio.rest import Client
import os

PH: "+12182503921"
OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = "AC7e0d7158ea646011d5212ed4fbf7ef97"

lat = 52.376060
lon = 5.784190
weather_params = {
    "lat": 23.022505,
    "lon": 72.571365,
    "appid": api_key,
    "exclude": "current,daily,minutely",
}
response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Its going to rain today. Remember to bring ☔️",
        from_="+12182503921",
        to='+46721262770'
    )
    print(message.status)