import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
api_key = os.getenv("OPENWEATHER_API_KEY")

twilio_phone_number = os.getenv("TWILIO_PHONE_NUMBER")
your_phone_number = os.getenv("YOUR_PHONE_NUMBER")

twilio_whatsapp_number = os.getenv("TWILIO_WHATSAPP_NUMBER")
your_whatsapp_number = os.getenv("YOUR_WHATSAPP_NUMBER")

weather_params = {
    "lat": 19.203515,
    "lon": 72.850000,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(OWN_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
#weather_slice = weather_data["list"]

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        
if will_rain:
    client = Client(account_sid, auth_token)
    
    # Send SMS
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella.☔",
        from_=twilio_phone_number,
        to=your_phone_number
    )
    print("SMS:", message.status)
        
    
    # Send WhatsApp message
    whatsapp_message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella. ☔",
        from_=f"whatsapp:{twilio_whatsapp_number}",
        to=f"whatsapp:{your_whatsapp_number}"
    )

    print("WhatsApp:", whatsapp_message.status)

else:
    print("No rain. No message sent.")