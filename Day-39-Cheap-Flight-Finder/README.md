✈️ Day 39/100 — Cheap Flight Finder API

A Cheap Flight Finder API built with Python and FastAPI that searches one-way flight prices using SerpAPI and sends a Twilio notification when the current price is lower than the target price stored in a Google Sheet.

This project is part of my 100 Days of Code — Python Backend Development Journey.

🚀 Project Overview

The application checks flight prices for routes stored in a Google Sheet.

For example:

Mumbai (BOM) → Varanasi (VNS)
Target Price → ₹5,000

The API searches the current one-way flight price.

If:

Current Price < Target Price

then the application sends a notification using Twilio.

🔄 Application Flow
Google Sheet
     ↓
Sheety API
     ↓
FastAPI
     ↓
SerpAPI Google Flights
     ↓
Current Flight Price
     ↓
Compare with Target Price
     ↓
Price is cheaper?
    /        \
  YES         NO
   ↓           ↓
Twilio      No Action
   ↓
📱 Notification
🛠️ Tech Stack
🐍 Python
⚡ FastAPI
✈️ SerpAPI — Google Flights
📊 Sheety API — Google Sheets
📱 Twilio — SMS Notification
🔐 python-dotenv — Environment Variables
⚡ requests-cache — API Response Caching
🚀 Uvicorn — ASGI Server
📁 Project Structure
Day-39-Cheap-Flight-Finder/
│
├── main.py
├── data_manager.py
├── flight_search.py
├── flight_data.py
├── notification_manager.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
File Responsibilities
File	Responsibility
main.py	FastAPI application and API endpoints
data_manager.py	Reads flight routes from Google Sheets using Sheety
flight_search.py	Searches one-way flights using SerpAPI
flight_data.py	Structures flight information
notification_manager.py	Sends notifications using Twilio
.env	Stores API credentials securely
📊 Google Sheet

The application reads flight routes and target prices from Google Sheets.

Example:

id	fromCity	fromIata	toCity	toIata	lowestPrice
2	Mumbai	BOM	Varanasi	VNS	5000
Example
Mumbai → Varanasi
BOM → VNS
Target Price → ₹5,000
🔌 API Endpoints
1. Home
GET /

Returns basic API information.

2. Get Flight Routes
GET /flights/sheet

Reads the available flight routes from Google Sheets.

Example response:

{
  "count": 1,
  "flights": [
    {
      "id": 2,
      "fromCity": "Mumbai",
      "fromIata": "BOM",
      "toCity": "Varanasi",
      "toIata": "VNS",
      "lowestPrice": 5000
    }
  ]
}
3. Search Flight
POST /flights/search

Searches for a one-way flight using SerpAPI.

Request:

{
  "from_iata": "BOM",
  "to_iata": "VNS",
  "outbound_date": "2026-09-15"
}

Example response:

{
  "price": 9604,
  "currency": "INR",
  "origin_airport": "BOM",
  "destination_airport": "VNS",
  "outbound_date": "2026-09-15",
  "airline": "IndiGo",
  "duration_minutes": 140
}
4. Check Cheap Flight Deal
POST /flights/check-deal

This is the main endpoint.

It:

Searches the current flight price.
Reads the target price from Google Sheets.
Compares the two prices.
Sends a Twilio notification if the flight is cheaper.

Request:

{
  "from_iata": "BOM",
  "to_iata": "VNS",
  "outbound_date": "2026-09-15"
}
💰 Price Comparison

Suppose Google Sheet contains:

Target Price = ₹5,000

SerpAPI finds:

Current Price = ₹4,500

The application checks:

₹4,500 < ₹5,000

Result:

✅ Cheap flight found
       ↓
📱 Twilio notification

If the current price is:

₹9,604

then:

₹9,604 < ₹5,000

is false.

Result:

❌ No cheaper flight

No notification is sent.

📱 Twilio Notification

When a cheaper flight is found, a message similar to this is sent:

✈️ CHEAP FLIGHT ALERT!


BOM → VNS
Price: ₹4,500
Airline: IndiGo
Departure: 2026-09-15
Duration: 140 minutes


Previous lowest price: ₹5,000
⚙️ Setup
1. Clone the Repository
git clone <your-repository-url>
cd Day-39-Cheap-Flight-Finder
2. Create Virtual Environment
python -m venv venv
Windows
venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt

Or install manually:

pip install fastapi uvicorn requests requests-cache python-dotenv twilio
4. Configure Environment Variables

Create a .env file:

SHEETY_ENDPOINT=your_sheety_endpoint


SERPAPI_KEY=your_serpapi_key


TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_FROM_NUMBER=your_twilio_from_number
TWILIO_TO_NUMBER=your_twilio_to_number
🔐 Important

Never commit .env to GitHub.

Add it to .gitignore:

.env
venv/
__pycache__/
*.pyc
flight_search_cache.sqlite
▶️ Run the Application

Start the FastAPI server:

uvicorn main:app --reload

The API will be available at:

http://127.0.0.1:8000
📚 Swagger API Documentation

FastAPI automatically provides interactive API documentation.

Open:

http://127.0.0.1:8000/docs

You can test all endpoints directly from Swagger UI.

🧪 Example Workflow
Step 1 — Add route to Google Sheet
Mumbai → Varanasi
BOM → VNS
Target Price → ₹5,000
Step 2 — Call API
POST /flights/check-deal
Step 3 — SerpAPI searches
BOM → VNS
Step 4 — Price comparison
Current Price → ₹4,500
Target Price → ₹5,000
Step 5 — Notification
₹4,500 < ₹5,000
       ↓
📱 Twilio SMS
🧠 What I Learned

Through this project, I practiced:

Building REST APIs with FastAPI
Working with external APIs
Integrating SerpAPI Google Flights
Reading data from Google Sheets using Sheety
Using Pydantic models for request validation
Using dataclasses to structure flight data
Working with environment variables
Protecting API credentials
Implementing price comparison logic
Sending SMS notifications using Twilio
API response caching with requests-cache
Organizing a project using separate classes and responsibilities
🔐 Security

API credentials are stored in environment variables instead of being hardcoded.

.env

is excluded from Git using:

.gitignore

No API keys or Twilio credentials should be committed to the repository.

🎯 Future Improvements

Possible improvements for this project:

 Add multiple flight routes
 Search multiple dates
 Add return/round-trip flight support
 Add airline filtering
 Add non-stop flight filtering
 Add WhatsApp notifications
 Add scheduled/background price checks
 Store historical flight prices
 Add PostgreSQL
 Add authentication
 Add frontend dashboard
 Deploy the FastAPI application
🚀 Learning in Public

Day 39/100 — Python Backend Development

This project helped me combine multiple concepts into one practical backend application:

Python
   +
FastAPI
   +
External APIs
   +
Google Sheets
   +
Flight Search
   +
Notifications

Another step forward in my Python Backend Developer journey. 🚀

👨‍💻 Author

Bipin Yadav

Python Backend Developer | FastAPI | PostgreSQL | SQLAlchemy

100 Days of Code — Python Backend Development Journey