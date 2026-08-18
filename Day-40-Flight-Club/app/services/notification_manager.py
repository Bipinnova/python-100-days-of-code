import os
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv
from twilio.rest import Client

from app.services.flight_data import FlightData


load_dotenv()


class NotificationManager:

    def __init__(self):

        # -------------------------
        # Twilio
        # -------------------------

        self.twilio_sid = os.getenv(
            "TWILIO_ACCOUNT_SID"
        )

        self.twilio_auth_token = os.getenv(
            "TWILIO_AUTH_TOKEN"
        )

        self.twilio_from = os.getenv(
            "TWILIO_FROM_NUMBER"
        )

        self.twilio_to = os.getenv(
            "TWILIO_TO_NUMBER"
        )

        # -------------------------
        # Email
        # -------------------------

        self.smtp_host = os.getenv(
            "SMTP_HOST",
            "smtp.gmail.com"
        )

        self.smtp_port = int(
            os.getenv(
                "SMTP_PORT",
                "587"
            )
        )

        self.smtp_email = os.getenv(
            "SMTP_EMAIL"
        )

        self.smtp_app_password = os.getenv(
            "SMTP_APP_PASSWORD"
        )

    def create_message(
        self,
        flight: FlightData
    ) -> str:

        if flight.stops == 0:

            flight_type = "Direct flight"

        elif flight.stops == 1:

            flight_type = "1-stop flight"

        else:

            flight_type = (
                f"{flight.stops}-stop flight"
            )

        return (
            f"✈️ Cheap Flight Alert!\n\n"
            f"{flight.origin_airport} → "
            f"{flight.destination_airport}\n\n"
            f"💰 Price: "
            f"{flight.currency} "
            f"{flight.price:,.0f}\n"
            f"📅 Date: "
            f"{flight.outbound_date}\n"
            f"🏷️ Airline: "
            f"{flight.airline or 'Unknown'}\n"
            f"🛫 Type: "
            f"{flight_type}\n"
            f"⏱️ Duration: "
            f"{flight.duration_minutes or 'Unknown'} minutes\n"
        )

    def send_whatsapp(
        self,
        flight: FlightData
    ) -> bool:

        if not all([
            self.twilio_sid,
            self.twilio_auth_token,
            self.twilio_from,
            self.twilio_to
        ]):

            print(
                "Twilio credentials are missing."
            )

            return False

        message_body = self.create_message(
            flight
        )

        client = Client(
            self.twilio_sid,
            self.twilio_auth_token
        )

        message = client.messages.create(
            body=message_body,
            from_=self.twilio_from,
            to=self.twilio_to
        )

        print(
            f"WhatsApp notification sent: "
            f"{message.sid}"
        )

        return True

    def send_email(
        self,
        recipient_email: str,
        flight: FlightData
    ) -> bool:

        if not all([
            self.smtp_email,
            self.smtp_app_password
        ]):

            print(
                "SMTP credentials are missing."
            )

            return False

        message_body = self.create_message(
            flight
        )

        email = EmailMessage()

        email["Subject"] = (
            f"Cheap Flight: "
            f"{flight.origin_airport} → "
            f"{flight.destination_airport}"
        )

        email["From"] = self.smtp_email

        email["To"] = recipient_email

        email.set_content(
            message_body
        )

        with smtplib.SMTP(
            self.smtp_host,
            self.smtp_port
        ) as server:

            server.starttls()

            server.login(
                self.smtp_email,
                self.smtp_app_password
            )

            server.send_message(
                email
            )

        print(
            f"Email sent to {recipient_email}"
        )

        return True

    def send_to_customers(
        self,
        customers,
        flight: FlightData
    ) -> int:

        sent_count = 0

        for customer in customers:

            try:

                if self.send_email(
                    customer.email,
                    flight
                ):
                    sent_count += 1

            except Exception as error:

                print(
                    f"Failed to send email "
                    f"to {customer.email}: "
                    f"{error}"
                )

        return sent_count