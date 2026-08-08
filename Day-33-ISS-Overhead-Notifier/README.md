# 🛰️ Day 33 - ISS Overhead Notifier

> **Part of my #100DaysOfCode Journey**

For Day 33 of my **#100DaysOfCode** challenge, I built an **ISS Overhead Notifier** using Python.

The application continuously checks the current location of the **International Space Station (ISS)** using an API. It compares the ISS location with my location and checks whether it is currently dark outside.

When the ISS is close to my location and it is dark enough to see it, the application automatically sends me an email notification telling me to look up at the sky.

---

# 🎯 Project Objectives

This project helped me revisit and strengthen my understanding of:

- REST APIs
- HTTP Requests
- JSON Data
- Geographic Coordinates
- Date & Time
- Conditional Logic
- Email Automation
- Continuous Monitoring
- Exception Handling

---

# 🛠️ How the Project Works

The application follows this workflow:

```text
             ┌──────────────────────┐
             │ Start Application    │
             └──────────┬───────────┘
                        ↓
             ┌──────────────────────┐
             │ Get ISS Location     │
             │ from API             │
             └──────────┬───────────┘
                        ↓
             ┌──────────────────────┐
             │ Compare ISS Location │
             │ with My Location     │
             └──────────┬───────────┘
                        ↓
                 ISS Nearby?
                   /      \
                 No        Yes
                 ↓          ↓
               Wait    Check Sunset
                            ↓
                       Is it Dark?
                        /      \
                      No        Yes
                      ↓          ↓
                    Wait    Send Email
```

---

# 📍 Location

The application uses latitude and longitude coordinates to determine whether the ISS is close to my location.

```python
MY_LAT = 19.200979
MY_LONG = 72.829968
```

The project considers the ISS to be nearby when its latitude and longitude are within approximately **±5 degrees** of the configured location.

---

# 🛰️ ISS Location API

The application sends an HTTP request to retrieve the ISS's current position.

The response contains:

- ISS Latitude
- ISS Longitude

The JSON response is then converted into Python data and used for comparison.

---

# 🌅 Sunrise & Sunset API

The application also checks whether it is currently dark.

It sends the configured latitude and longitude to a sunrise/sunset API and retrieves:

- Sunrise time
- Sunset time

The application then compares these times with the current time.

---

# 📧 Email Notification

When both conditions are satisfied:

1. The ISS is close to the configured location.
2. It is currently dark.

The application sends an email notification:

```text
Subject: Look Up 👆🏻

The ISS is above you in the sky.
```

---

# 💡 Key Concepts Revisited

## 🐍 Python

- Functions
- Conditional Statements
- Loops
- Variables
- Type Conversion
- Exception Handling

---

## 🌐 APIs

- HTTP GET Requests
- Query Parameters
- JSON Responses
- API Status Codes
- `requests` Library

---

## 📍 Location & Time

- Latitude
- Longitude
- datetime
- Sunrise
- Sunset
- Time Comparison

---

## 📧 Email Automation

- SMTP
- Gmail SMTP
- TLS
- Automated Email Notifications

---

# 🛠️ Technologies Used

- Python
- Requests
- REST APIs
- JSON
- datetime
- smtplib

---

# 🚀 Features

- ✅ Real-Time ISS Location Tracking
- ✅ Location-Based Detection
- ✅ Sunrise & Sunset Detection
- ✅ Automatic Dark-Sky Detection
- ✅ Continuous Monitoring
- ✅ Email Notification
- ✅ API Integration
- ✅ Automated Workflow

---

# 📂 Project Structure

```text
Day-33-ISS-Overhead-Notifier/
│
├── main.py
├── README.md
└── requirements.txt
```

---

# 📦 Installation

Install the required dependency:

```bash
pip install requests
```

---

# ▶️ Run the Application

```bash
python main.py
```

The application continuously checks the ISS location and sky conditions.

When the conditions are satisfied, an email notification is sent automatically.

---

# 🔐 Security Note

**Never store your email password or API credentials directly in the source code.**

For example, avoid:

```python
MY_PASSWORD = "your-password"
```

Instead, use environment variables:

```python
import os

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
```

Create environment variables before running the application.

Also, if an email App Password has been accidentally committed to GitHub or shared publicly, **revoke it immediately and generate a new one.**

---

# 📖 What I Reinforced Today

- REST API Integration
- HTTP Requests
- JSON Data Processing
- Location-Based Logic
- Date & Time Handling
- SMTP Email Automation
- Continuous Monitoring
- Conditional Logic

---

# 💡 Engineering Takeaway

This project reinforced how multiple external services can be combined to create an automated real-world application.

Instead of simply retrieving data from an API, the application combines **ISS location data, geographic coordinates, sunrise/sunset information, time-based logic, and email automation** to make a useful decision and notify the user automatically.

It was a great exercise in connecting independent components together into an automated workflow.

---

**🚀 Revisiting Python Fundamentals | Building Better Software Every Day**