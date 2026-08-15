# 🏋️ Day 38 — Exercise Tracker API | 100 Days of Code

Welcome to **Day 38** of my **#100DaysOfCode** journey.

Today, I built an **Exercise Tracker REST API** using **Python and FastAPI** that accepts natural-language exercise descriptions, calculates exercise duration and calories burned using an external API, and automatically stores the workout data in **Google Sheets** through the **Sheety API**.

---

## 🚀 What I Built

The Exercise Tracker allows users to enter natural-language exercise information such as:

> `I ran 5K and cycled for 20 minutes.`

The application then:

1. Receives the request through FastAPI.
2. Validates the input using Pydantic.
3. Sends the exercise description to the Exercise/Nutrition API.
4. Identifies the exercises and calculates duration and calories burned.
5. Sends the workout data to Sheety API.
6. Stores the results automatically in Google Sheets.

---

## 🔄 Project Flow

```text
User
  ↓
FastAPI REST API
  ↓
Pydantic Validation
  ↓
Exercise/Nutrition API
  ↓
Exercise + Duration + Calories
  ↓
Sheety API
  ↓
Google Sheets
```

---

## ✨ Features

* 🏃 Natural-language exercise input
* 🔢 Exercise duration detection
* 🔥 Calories burned calculation
* 🔗 External API integration
* ⚡ FastAPI REST API
* ✅ Pydantic request validation
* 📊 Automatic Google Sheets storage
* 🔐 Environment variable-based configuration
* 🛡️ Basic authentication for Sheety API
* ❌ Error handling for external API failures

---

## 🛠️ Tech Stack

* **Python**
* **FastAPI**
* **Pydantic**
* **Requests**
* **Nutrition/Exercise API**
* **Sheety API**
* **Google Sheets**
* **python-dotenv**
* **Uvicorn**

---

## 📁 Project Structure

```text
Day-38-Exercise-Tracker/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── schemas.py
│   │
│   └── services/
│       ├── __init__.py
│       ├── exercise_service.py
│       └── sheet_service.py
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🔌 API Endpoint

### Track Exercise

```http
POST /exercise
```

### Request

```json
{
  "exercise_text": "ran 5k and cycled for 20 minutes"
}
```

### Example Response

```json
{
  "message": "Exercise tracked successfully",
  "data": [
    {
      "exercise": "running",
      "duration": 30,
      "calories": 250
    },
    {
      "exercise": "cycling",
      "duration": 20,
      "calories": 150
    }
  ]
}
```

> The actual duration and calorie values are calculated by the external Exercise/Nutrition API and may vary.

---

## 📊 Google Sheets

After processing the request, the workout information is automatically stored in Google Sheets.

Example:

| Date       | Time     | Exercise | Duration | Calories |
| ---------- | -------- | -------- | -------: | -------: |
| 15/08/2026 | 09:30:00 | Running  |       30 |      250 |
| 15/08/2026 | 09:30:00 | Cycling  |       20 |      150 |

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the project

```bash
cd Day-38-Exercise-Tracker
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure environment variables

Create a `.env` file:

```env
ENV_NIX_APP_ID=your_app_id
ENV_NIX_API_KEY=your_api_key

ENV_SHEETY_ENDPOINT=your_sheety_endpoint
ENV_SHEETY_USERNAME=your_sheety_username
ENV_SHEETY_PASSWORD=your_sheety_password

GENDER=male
WEIGHT_KG=84
HEIGHT_CM=180
AGE=32
```

**Never commit `.env` to GitHub.**

---

## 🚀 Start the FastAPI Server

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

## 📚 API Documentation

FastAPI automatically provides interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

## 🧪 Example Test Inputs

```text
ran 5k and cycled for 20 minutes
```

```text
I walked for 30 minutes and did yoga for 15 minutes
```

```text
ran for 30 minutes and lifted weights for 20 minutes
```

```text
cycled for 45 minutes and swam for 20 minutes
```

---

## 🔐 Security

API credentials are stored using environment variables instead of being hard-coded in the application.

The `.env` file should be added to `.gitignore`:

```gitignore
.env
venv/
__pycache__/
*.pyc
```

A `.env.example` file can be used to show the required environment variables without exposing real credentials.

---

## 🎯 What I Learned

Through this project, I practiced:

* Building REST APIs with **FastAPI**
* Request validation using **Pydantic**
* Integrating third-party APIs
* Working with external API authentication
* Handling API responses and errors
* Using environment variables securely
* Connecting FastAPI with Google Sheets through Sheety
* Structuring a backend application using service layers
* Testing APIs using Swagger UI

---

## 🚀 Future Improvements

* [ ] Add PostgreSQL database
* [ ] Add user authentication with JWT
* [ ] Add workout history endpoints
* [ ] Add update/delete workout functionality
* [ ] Add weekly/monthly workout summaries
* [ ] Add total calories burned statistics
* [ ] Add frontend dashboard
* [ ] Dockerize the application

---

## 📌 Day 38 Progress

**Project:** Exercise Tracker API

**Focus:** FastAPI + External API Integration

**Status:** ✅ Completed

---

## 📖 100 Days of Code

This project is part of my **100 Days of Code** journey, where I am consistently building projects and strengthening my Python backend development skills.

**Day 38 / 100 🚀**

#Python #FastAPI #RESTAPI #BackendDevelopment #APIs #100DaysOfCode #PythonDeveloper
