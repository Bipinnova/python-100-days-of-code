import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client
from fastapi import FastAPI, HTTPException

load_dotenv()

app = FastAPI(
    title="Stock Trading News Alert API",
    description="Get stock movement, related news, SMS and WhatsApp alerts.",
    version="1.0.0"
)

# STOCK_NAME = "TSLA"
# COMPANY_NAME = "Tesla Inc"

STOCK_NAME = "VRTX"
COMPANY_NAME = "Vertex Pharmaceuticals"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

stock_api_key = os.getenv("STOCK_API_KEY")
news_api_key = os.getenv("NEWS_API_KEY")

twilio_phone_number = os.getenv("TWILIO_PHONE_NUMBER")
your_phone_number = os.getenv("YOUR_PHONE_NUMBER")

twilio_whatsapp_number = os.getenv("TWILIO_WHATSAPP_NUMBER")
your_whatsapp_number = os.getenv("YOUR_WHATSAPP_NUMBER")


# ============================================
# Helper: Get Stock Data
# ============================================

def get_stock_data():

    stock_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_NAME,
        "apikey": stock_api_key
    }

    response = requests.get(
        STOCK_ENDPOINT,
        params=stock_params
    )

    response.raise_for_status()

    data = response.json()

    if "Time Series (Daily)" not in data:
        raise HTTPException(
            status_code=502,
            detail={
                "message": "Stock API did not return daily data",
                "response": data
            }
        )

    time_series = data["Time Series (Daily)"]

    data_list = [
        value
        for key, value in time_series.items()
    ]

    yesterday_data = data_list[0]

    yesterday_closing_price = float(
        yesterday_data["4. close"]
    )

    day_before_yesterday_data = data_list[1]

    day_before_yesterday_closing_price = float(
        day_before_yesterday_data["4. close"]
    )

    difference = (
        yesterday_closing_price -
        day_before_yesterday_closing_price
    )

    if difference > 0:
        up_or_down = "🔺"
    elif difference < 0:
        up_or_down = "🔻"
    else:
        up_or_down = "➡️"

    diff_percent = round(
        abs(difference) /
        day_before_yesterday_closing_price
        * 100,
        2
    )

    return {
        "stock": STOCK_NAME,
        "company": COMPANY_NAME,
        "yesterday_closing_price": yesterday_closing_price,
        "day_before_yesterday_closing_price": day_before_yesterday_closing_price,
        "difference": round(difference, 2),
        "direction": up_or_down,
        "percentage_change": diff_percent
    }


# ============================================
# Helper: Get News
# ============================================

def get_news():

    news_params = {
        "q": COMPANY_NAME,
        "apiKey": news_api_key,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 3
    }

    response = requests.get(
        NEWS_ENDPOINT,
        params=news_params
    )

    response.raise_for_status()

    data = response.json()

    if data.get("status") != "ok":
        raise HTTPException(
            status_code=502,
            detail=data
        )

    articles = data.get("articles", [])

    return articles[:3]


# ============================================
# Helper: Send Notifications
# ============================================

def send_notifications(messages):

    client = Client(
        account_sid,
        auth_token
    )

    results = []

    for message_text in messages:
        # print("Sending SMS...")
        # SMS
        sms_message = client.messages.create(
            body=message_text,
            from_=twilio_phone_number,
            to=your_phone_number
        )
        
        # print("SMS SID:", sms_message.sid)
        # print("SMS Status:", sms_message.status)
        
        # print("Sending WhatsApp...")

        # WhatsApp
        whatsapp_message = client.messages.create(
            body=message_text,
            from_=f"whatsapp:{twilio_whatsapp_number}",
            to=f"whatsapp:{your_whatsapp_number}"
        )
        
        # print("WhatsApp SID:", whatsapp_message.sid)
        # print("WhatsApp Status:", whatsapp_message.status)

        results.append({
            # "sms_sid": sms_message.sid,
            "sms_status": sms_message.status,
            # "whatsapp_sid": whatsapp_message.sid,
            "whatsapp_status": whatsapp_message.status
        })

    return results


# ============================================
# GET /
# ============================================

@app.get("/", include_in_schema=False)
def home():

    return {
        "message": "Stock Trading News Alert API",
        "stock": STOCK_NAME,
        "company": COMPANY_NAME,
        "docs": "/docs"
    }


# ============================================
# GET /stock
# ============================================

@app.get("/stock")
def stock():

    return get_stock_data()


# ============================================
# GET /news
# ============================================

@app.get("/news")
def news():

    stock_data = get_stock_data()

    if stock_data["percentage_change"] <= 5:
        return {
            "message": "Stock movement is not greater than 5%",
            "stock_data": stock_data,
            "articles": []
        }

    articles = get_news()

    return {
        "stock_data": stock_data,
        "articles": [
            {
                "title": article["title"],
                "description": article["description"],
                "url": article["url"]
            }
            for article in articles
        ]
    }


# ============================================
# POST /send-alert
# ============================================

@app.post("/send-alert")
def send_alert():

    stock_data = get_stock_data()

    # Don't send news if movement is <= 5%
    if stock_data["percentage_change"] <= 5:

        return {
            "message": "No alert sent",
            "reason": "Stock movement is not greater than 5%",
            "stock_data": stock_data
        }

    articles = get_news()

    if not articles:

        return {
            "message": "Stock moved more than 5%, but no news articles were found.",
            "stock_data": stock_data
        }

    formatted_articles = [
        (
            f"{STOCK_NAME}: "
            f"{stock_data['direction']}"
            f"{stock_data['percentage_change']}%\n"
            f"Headline: {article['title']}\n"
            f"Brief: "
            f"{article['description'] or 'No description available.'}"
        )
        for article in articles
    ]

    notification_results = send_notifications(
        formatted_articles
    )

    return {
        "message": "Stock alert sent successfully",
        "stock_data": stock_data,
        "articles_sent": len(formatted_articles),
        "notifications": notification_results
    }