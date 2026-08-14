import os

from dotenv import load_dotenv


load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")



#PIXELA_BASE_URL = "https://pixe.la/v1"
# PIXELA_USERNAME = os.getenv("PIXELA_USERNAME")
# PIXELA_TOKEN = os.getenv("PIXELA_TOKEN")


PIXELA_BASE_URL = os.getenv(
    "PIXELA_BASE_URL",
    "https://pixe.la/v1"
)


PIXELA_USERNAME = os.getenv("PIXELA_USERNAME")
PIXELA_TOKEN = os.getenv("PIXELA_TOKEN")

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_ALGORITHM = os.getenv(
    "JWT_ALGORITHM",
    "HS256"
)

JWT_ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv(
        "JWT_ACCESS_TOKEN_EXPIRE_MINUTES",
        "30"
    )
)