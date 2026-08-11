# 📈 Stock Trading News Alert API

A **FastAPI-based stock monitoring and news alert system** that checks daily stock price movement and sends the latest company news through **SMS and WhatsApp** when the stock price changes by more than **5%**.

This project was built as part of my **100 Days of Code – Python Backend Development** journey.

---

## 🚀 Project Overview

The application monitors a stock using the **Alpha Vantage API**.

It compares the closing prices of the latest two trading days.

If the stock price movement is greater than **5%**, the application:

1. 📊 Fetches stock price data from Alpha Vantage
2. 📈 Calculates the percentage change
3. 📰 Fetches the latest company news using NewsAPI
4. 📱 Sends the news through SMS using Twilio
5. 💬 Sends the same news through WhatsApp using Twilio

The project exposes this functionality through a **FastAPI REST API** with interactive Swagger documentation.

---

## 🏗️ Architecture

```text
                    ┌─────────────────────┐
                    │     FastAPI API     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Alpha Vantage     │
                    │    Stock Data       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Calculate Stock     │
                    │ Percentage Change   │
                    └──────────┬──────────┘
                               │
                         > 5% ?
                         /     \
                       No       Yes
                       │         │
                       ▼         ▼
                    No Alert   NewsAPI
                                  │
                                  ▼
                         Latest 3 Articles
                                  │
                                  ▼
                         ┌────────────────┐
                         │     Twilio      │
                         └───────┬────────┘
                            ┌────┴────┐
                            ▼         ▼
                           SMS     WhatsApp
```

---

## ✨ Features

* ✅ FastAPI REST API
* ✅ Stock price monitoring
* ✅ Percentage change calculation
* ✅ Configurable 5% alert threshold
* ✅ Latest company news
* ✅ NewsAPI integration
* ✅ Twilio SMS notifications
* ✅ Twilio WhatsApp notifications
* ✅ Environment variable configuration
* ✅ Swagger/OpenAPI documentation
* ✅ Error handling for external API failures
* ✅ Separate endpoints for stock, news, and alerts

---

## 🛠️ Technologies Used

* **Python**
* **FastAPI**
* **REST API**
* **Alpha Vantage API**
* **NewsAPI**
* **Twilio API**
* **python-dotenv**
* **Requests**
* **Uvicorn**

---

## 📁 Project Structure

```text
Day-36-Stock-Trading-News-Alert/
│
├── main.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token

STOCK_API_KEY=your_alpha_vantage_api_key
NEWS_API_KEY=your_news_api_key

TWILIO_PHONE_NUMBER=your_twilio_phone_number
YOUR_PHONE_NUMBER=your_phone_number

TWILIO_WHATSAPP_NUMBER=your_twilio_whatsapp_number
YOUR_WHATSAPP_NUMBER=your_whatsapp_number
```

⚠️ **Never commit your `.env` file or API keys to GitHub.**

Add this to `.gitignore`:

```text
.env
__pycache__/
*.pyc
```

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/python-100-days-of-code.git
```

Go to the project directory:

```bash
cd Day-36-Stock-Trading-News-Alert
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

## 📚 API Documentation

FastAPI automatically provides interactive Swagger documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

Available endpoints:

| Method | Endpoint      | Description                            |
| ------ | ------------- | -------------------------------------- |
| GET    | `/`           | API information                        |
| GET    | `/stock`      | Get stock price information            |
| GET    | `/news`       | Get company news when movement > 5%    |
| POST   | `/send-alert` | Send stock news through SMS & WhatsApp |

---

## 🔹 GET `/`

Returns basic information about the API.

Example:

```json
{
  "message": "Stock Trading News Alert API",
  "stock": "VRTX",
  "company": "Vertex Pharmaceuticals",
  "docs": "/docs"
}
```

---

## 🔹 GET `/stock`

Fetches the latest stock prices and calculates the percentage change.

Example response:

```json
{
  "stock": "VRTX",
  "company": "Vertex Pharmaceuticals",
  "yesterday_closing_price": 523.91,
  "day_before_yesterday_closing_price": 496.07,
  "difference": 27.84,
  "direction": "🔺",
  "percentage_change": 5.61
}
```

---

## 🔹 GET `/news`

If the stock movement is greater than 5%, the API fetches the latest three company-related news articles.

Example:

```json
{
  "stock_data": {
    "stock": "VRTX",
    "company": "Vertex Pharmaceuticals",
    "percentage_change": 5.61
  },
  "articles": [
    {
      "title": "Example headline",
      "description": "Example news description",
      "url": "https://example.com"
    }
  ]
}
```

If the movement is below 5%:

```json
{
  "message": "Stock movement is not greater than 5%",
  "articles": []
}
```

---

## 🔹 POST `/send-alert`

This is the main notification endpoint.

The API:

```text
Stock Data
    ↓
Calculate %
    ↓
Movement > 5%?
    ↓
   Yes
    ↓
Get 3 News Articles
    ↓
Twilio
 ┌──┴──┐
SMS  WhatsApp
```

Example response:

```json
{
  "message": "Stock alert sent successfully",
  "stock_data": {
    "stock": "VRTX",
    "percentage_change": 5.61
  },
  "articles_sent": 3,
  "notifications": [
    {
      "sms_status": "queued",
      "whatsapp_status": "queued"
    }
  ]
}
```

---

## 🔐 Security

Sensitive credentials are loaded using environment variables:

```python
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
stock_api_key = os.getenv("STOCK_API_KEY")
news_api_key = os.getenv("NEWS_API_KEY")
```

API keys and authentication credentials are **not hardcoded in the source code**.

---

## 🧠 What I Learned

Through this project, I practiced:

* Building REST APIs with FastAPI
* Working with external APIs
* HTTP requests using Python
* Processing JSON responses
* Calculating stock price changes
* Integrating multiple third-party services
* Environment variable management
* API error handling
* SMS and WhatsApp integration
* Swagger/OpenAPI testing
* Designing API endpoints
* Backend application structure

---

## 🔮 Future Improvements

Some improvements I would like to add:

* [ ] Support multiple stocks
* [ ] Add PostgreSQL database
* [ ] Store stock history
* [ ] Add user authentication with JWT
* [ ] Add user-specific alert thresholds
* [ ] Add background tasks
* [ ] Add scheduled stock monitoring
* [ ] Add Docker support
* [ ] Deploy the FastAPI API to the cloud
* [ ] Add automated tests with Pytest

---

## 🎯 Project Goal

The goal of this project was not to build a trading system or provide investment advice.

The main goal was to practice building a **real-world Python backend application** that integrates multiple APIs and delivers useful notifications through a REST API.

---

## 👨‍💻 100 Days of Code

**Day 36 / 100**

Continuing my journey to strengthen my **Python Backend Development and FastAPI skills** by building practical projects and learning in public.

---

## 📌 Disclaimer

This project is created for **educational and development purposes only**.

Stock price movements and news alerts are not investment advice.

---

⭐ If you find this project useful, feel free to explore the repository and connect with me on LinkedIn.
