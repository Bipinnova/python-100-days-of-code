# import os
# import requests
# from requests.auth import HTTPBasicAuth
# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()

# SHEETY_PRICES_ENDPOINT = os.environ["SHEETY_PRICES_ENDPOINT"]

# class DataManager:

#     def __init__(self):
#         self._user = os.environ["SHEETY_USERNAME"]
#         self._password = os.environ["SHEETY_PASSWORD"]
#         self._authorization = HTTPBasicAuth(self._user, self._password)
#         self.destination_data = {}

#     def get_destination_data(self):
#         response = requests.get(url=SHEETY_PRICES_ENDPOINT, auth=self._authorization)
#         data = response.json()
#         self.destination_data = data["prices"]
#         return self.destination_data

#     # ==================== Updated the price in the spreadsheet ====================

#     def update_lowest_price(self, row_id, new_price):
#         new_data = {
#             "price": {
#                 "lowestPrice": new_price
#             }
#         }
#         requests.put(
#             url=f"{SHEETY_PRICES_ENDPOINT}/{row_id}",
#             json=new_data,
#             auth=self._authorization
#         )
import os

import requests
from dotenv import load_dotenv


load_dotenv()


class DataManager:

    def __init__(self):
        self.endpoint = os.getenv("SHEETY_ENDPOINT")

        if not self.endpoint:
            raise ValueError("SHEETY_ENDPOINT is missing in .env")

    def get_flight_data(self):

        response = requests.get(
            self.endpoint,
            timeout=30
        )

        response.raise_for_status()

        data = response.json()

        return data.get("sheet1", [])


# if __name__ == "__main__":

#     manager = DataManager()

#     flights = manager.get_flight_data()

#     print(flights)