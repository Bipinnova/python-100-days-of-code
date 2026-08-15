# import os
# from dotenv import load_dotenv

# load_dotenv()


# NIX_APP_ID = os.getenv("ENV_NIX_APP_ID")
# NIX_API_KEY = os.getenv("ENV_NIX_API_KEY")

# SHEETY_ENDPOINT = os.getenv("ENV_SHEETY_ENDPOINT")
# SHEETY_USERNAME = os.getenv("ENV_SHEETY_USERNAME")
# SHEETY_PASSWORD = os.getenv("ENV_SHEETY_PASSWORD")

# GENDER = os.getenv("GENDER", "male")
# WEIGHT_KG = float(os.getenv("WEIGHT_KG", 75))
# HEIGHT_CM = float(os.getenv("HEIGHT_CM", 170))
# AGE = int(os.getenv("AGE", 25))

import os
from dotenv import load_dotenv

load_dotenv(override=True)

NIX_APP_ID = os.getenv("ENV_NIX_APP_ID")
NIX_API_KEY = os.getenv("ENV_NIX_API_KEY")

SHEETY_ENDPOINT = os.getenv("ENV_SHEETY_ENDPOINT")
SHEETY_USERNAME = os.getenv("ENV_SHEETY_USERNAME")
SHEETY_PASSWORD = os.getenv("ENV_SHEETY_PASSWORD")

GENDER = os.getenv("GENDER", "male")
WEIGHT_KG = float(os.getenv("WEIGHT_KG", 84))
HEIGHT_CM = float(os.getenv("HEIGHT_CM", 180))
AGE = int(os.getenv("AGE", 32))