# ☕ Day 16 - Coffee Machine REST API using FastAPI

A RESTful Coffee Machine API built with **Python**, **Object-Oriented Programming (OOP)**, and **FastAPI** as part of my **#100DaysOfCode** journey.

This project converts the classic console-based Coffee Machine application into a modern REST API with interactive Swagger documentation.

---

## 🚀 Features

* View all available coffee drinks
* View coffee prices
* Order coffee
* Check available machine resources
* Track machine profit
* Validate available resources before preparing coffee
* Validate payment before serving coffee
* Interactive API documentation using Swagger UI

---

## 🛠️ Tech Stack

* Python 3
* FastAPI
* Uvicorn
* Pydantic
* Object-Oriented Programming (OOP)

---

## 📂 Project Structure

```text
Day-16-Coffee-Machine-using-OOP/
│
├── app/
│   ├── main.py
│   │
│   ├── models/
│   │   ├── coffee_maker.py
│   │   ├── menu.py
│   │   └── money_machine.py
│   │
│   ├── schemas/
│   │   └── coffee.py
│   │
│   └── services/
│       └── coffee_service.py
│
├── requirements.txt
├── run.py
└── README.md
```

---

# 📌 API Endpoints

## Home

**GET /**

Returns the welcome message.

---

## Get Menu

**GET /menu**

Returns all available coffee drinks along with their prices.

Example Response

```json
{
  "available_drinks": [
    {
      "name": "espresso",
      "price": 125,
      "ingredients": {
        "water": 50,
        "milk": 0,
        "coffee": 18
      }
    },
    {
      "name": "latte",
      "price": 200,
      "ingredients": {
        "water": 200,
        "milk": 150,
        "coffee": 24
      }
    },
    {
      "name": "cappuccino",
      "price": 250,
      "ingredients": {
        "water": 250,
        "milk": 50,
        "coffee": 24
      }
    }
  ]
}
```

---

## Order Coffee

**POST /order**

Request

```json
{
    "drink_name":"latte",
    "amount":250
}
```

Success Response

```json
{
    "success": true,
    "message": "latte is ready.",
    "change": 50
}
```

---

## Machine Report

**GET /report**

Example Response

```json
{
    "resources": "How much of each item the machine has.",
    "water": "300 ml",
    "milk": "200 ml",
    "coffee": "100 grams",
    "profit": "The money the machine made. It is currently ₹125."
}
```

---

# ▶️ How to Run

## Clone the repository

```bash
git clone https://github.com/<your-username>/python-100-days-of-code.git
```

---

## Navigate to the project

```bash
cd Day-16-Coffee-Machine-using-OOP
```

---

## Create Virtual Environment

Windows

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

---

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the server

```bash
python run.py
```

or

```bash
uvicorn app.main:app --reload
```

---

## Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

# 📚 Concepts Practiced

## Python

* Classes and Objects
* Constructors (`__init__`)
* Methods
* Dictionaries
* Lists
* Loops
* Conditional Statements
* Function Calls
* Return Values

---

## Object-Oriented Programming (OOP)

* Encapsulation
* Object Composition
* Class Design
* Separation of Responsibilities
* Reusable Components

---

## FastAPI

* FastAPI Application
* Path Operations
* GET Requests
* POST Requests
* Request Body Validation
* JSON Responses
* HTTP Exception Handling
* Swagger UI Documentation

---

## Pydantic

* Request Models
* Data Validation
* Automatic Request Parsing

---

## API Design

* REST API Development
* Resource Validation
* Business Logic Layer
* Service Layer
* Clean Project Structure

---

# 📖 Learning Outcome

Through this project I learned how to:

* Convert a console application into a REST API.
* Organize a FastAPI project using models, schemas, and services.
* Apply Object-Oriented Programming principles in a real project.
* Validate incoming API requests using Pydantic.
* Build clean and maintainable backend applications.
* Expose interactive API documentation with Swagger UI.

---

# 🎯 Future Improvements

* SQLAlchemy Integration
* PostgreSQL Database
* JWT Authentication
* User Accounts
* Order History
* Dependency Injection
* Docker Support
* Unit Testing with Pytest
* Logging
* CI/CD Pipeline

---

# 📸 API Documentation

FastAPI automatically generates interactive API documentation.

Swagger UI

```
http://127.0.0.1:8000/docs
```

Redoc

```
http://127.0.0.1:8000/redoc
```

---

# 👨‍💻 Author

**Bipin Yadav**

Python Backend Developer | FastAPI | PostgreSQL | REST APIs

Currently building real-world backend projects as part of my **#100DaysOfCode** journey.
