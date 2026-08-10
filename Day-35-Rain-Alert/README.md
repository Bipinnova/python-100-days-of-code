# 🌧️ Day 35 - Rain Alert Automation

> Part of my #100DaysOfCode Journey

For Day 35, I built a **Rain Alert Automation** system using Python.

The application checks the weather forecast using the **OpenWeather API**. If rain is expected, it automatically sends an alert through both **SMS and WhatsApp using Twilio**.

---

# 🎯 Project Objective

The goal was to combine external APIs and automation to create a practical weather notification system.

---

# 🚀 How It Works

```text
OpenWeather API
       ↓
Get Weather Forecast
       ↓
Check Weather Conditions
       ↓
Rain Expected?
    ↓        ↓
   Yes       No
    ↓        ↓
Twilio     No Alert
    ↓
SMS + WhatsApp
```

---

# 🛠️ Features

- ✅ Weather Forecast API Integration
- ✅ Rain Detection
- ✅ Automatic SMS Alert
- ✅ Automatic WhatsApp Alert
- ✅ Environment Variable Configuration
- ✅ API Error Handling
- ✅ Automated Notifications

---

# 🔍 Concepts Reinforced

### Python

- Functions
- Loops
- Conditional Statements
- Environment Variables
- Exception Handling

### APIs

- REST API Integration
- HTTP GET Requests
- JSON Response Processing
- API Parameters

### Automation

- Weather Monitoring
- Conditional Notifications
- SMS Automation
- WhatsApp Automation

---

# 🛠️ Technologies Used

- Python
- Requests
- OpenWeather API
- Twilio
- python-dotenv

---

# 🔐 Environment Variables

API keys and credentials should never be hardcoded.

Create a `.env` file:

```env
OPENWEATHER_API_KEY=your_api_key
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE_NUMBER=your_twilio_number
YOUR_PHONE_NUMBER=your_phone_number
TWILIO_WHATSAPP_NUMBER=your_whatsapp_number
YOUR_WHATSAPP_NUMBER=your_whatsapp_number
```

Add `.env` to `.gitignore`.

---

# 📦 Installation

Install the required packages:

```bash
pip install requests python-dotenv twilio
```

---

# ▶️ Run the Application

```bash
python main.py
```

The application checks the upcoming weather forecast and sends an alert when rain is detected.

---

# 💡 Engineering Takeaway

This project reinforced how multiple external APIs can be combined to build a practical automation workflow.

By connecting a weather API with Twilio, a simple Python script can automatically monitor conditions and deliver notifications through multiple communication channels.

---

# 📈 Challenge Progress

**35/100 Days Completed**

🚀 Revisiting Python Fundamentals | Building Better Software Every Day