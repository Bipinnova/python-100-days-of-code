import os

from dotenv import load_dotenv
from twilio.rest import Client


load_dotenv()


class NotificationManager:

    def __init__(self):

        account_sid = os.getenv(
            "TWILIO_ACCOUNT_SID"
        )

        auth_token = os.getenv(
            "TWILIO_AUTH_TOKEN"
        )

        if not account_sid:
            raise ValueError(
                "TWILIO_ACCOUNT_SID is missing in .env"
            )

        if not auth_token:
            raise ValueError(
                "TWILIO_AUTH_TOKEN is missing in .env"
            )

        self.client = Client(
            account_sid,
            auth_token
        )

        self.from_number = os.getenv(
            "TWILIO_FROM_NUMBER"
        )

        self.to_number = os.getenv(
            "TWILIO_TO_NUMBER"
        )

    def send_notification(self, message):

        sms = self.client.messages.create(
            body=message,
            from_=self.from_number,
            to=self.to_number
        )

        return sms.sid