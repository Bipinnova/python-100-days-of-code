# 🎯 Day 34 - Dynamic Quiz App with API & Tkinter

> Part of my #100DaysOfCode Journey

For Day 34, I revisited my previous **Quiz Game project from Day 17** and upgraded it from a static quiz application into a **dynamic GUI-based Quiz App**.

Instead of storing questions directly inside the Python project, the application now fetches questions dynamically from the **Open Trivia Database API**.

The quiz is presented through a Tkinter GUI with True/False buttons, instant visual feedback, and score tracking.

---

# 🎯 Project Objectives

This project helped me revisit and strengthen my understanding of:

- REST API Integration
- JSON Data Processing
- Object-Oriented Programming
- Tkinter GUI Development
- API Data Mapping
- Business Logic Separation
- Event-Driven Programming
- Dynamic Data Handling

---

# 🔄 Day 17 → Day 34

This project builds on the Quiz API project I created earlier.

### Day 17

The quiz questions were stored locally in Python.

```text
Python Data
     ↓
QuizBrain
     ↓
Quiz API
```

### Day 34

The questions are now fetched dynamically from an external API.

```text
Open Trivia Database API
          ↓
      JSON Data
          ↓
    Question Objects
          ↓
      QuizBrain
          ↓
      Tkinter GUI
```

This upgrade makes the application more dynamic and allows the quiz questions to be changed without modifying the source code.

---

# 🛠️ How the Application Works

## Step 1 - Fetch Questions

The application sends a GET request to the Open Trivia Database API.

```python
parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18,
}
```

The API returns quiz questions in JSON format.

---

## Step 2 - Process API Response

The JSON response is converted into Python data.

```python
response = requests.get(
    "https://opentdb.com/api.php",
    params=parameters
)

response.raise_for_status()

data = response.json()
```

---

## Step 3 - Create Question Objects

Each API question is converted into a `Question` object.

```python
new_question = Question(
    question_text,
    question_answer
)

question_bank.append(new_question)
```

This keeps the quiz data organized using Object-Oriented Programming.

---

## Step 4 - QuizBrain

`QuizBrain` manages the quiz logic.

Responsibilities include:

- Tracking the current question
- Tracking the score
- Checking whether questions remain
- Providing the next question
- Checking the user's answer

---

## Step 5 - Tkinter GUI

The user interacts with the quiz through a graphical interface.

The GUI provides:

- Question display
- True button
- False button
- Score display
- Instant answer feedback
- Final quiz message

---

# 🔍 Concepts Revisited

## 🌐 REST APIs

- HTTP GET Requests
- Query Parameters
- API Responses
- JSON Data
- `requests` Library
- `raise_for_status()`

---

## 🐍 Python

- Functions
- Lists
- Dictionaries
- Loops
- Modules
- Classes
- Objects

---

## 🧱 Object-Oriented Programming

- Classes
- Objects
- Encapsulation
- Separation of Responsibilities

---

## 🖥️ Tkinter

- Window Creation
- Labels
- Buttons
- Canvas
- Grid Layout
- Event Handling
- `after()` Scheduling

---

# 🚀 Features

- ✅ Dynamic Quiz Questions
- ✅ Open Trivia Database API
- ✅ True / False Quiz
- ✅ Tkinter GUI
- ✅ Instant Visual Feedback
- ✅ Score Tracking
- ✅ Automatic Question Progression
- ✅ API Data Processing
- ✅ Object-Oriented Quiz Logic

---

# 📂 Project Structure

```text
Day-34-GUI-Quiz-App/
│
├── main.py
├── quiz_brain.py
├── question_model.py
├── ui.py
├── images/
│   ├── true.png
│   └── false.png
│
└── README.md
```

---

# 📦 Technologies Used

- Python
- Tkinter
- Requests
- REST API
- JSON
- Object-Oriented Programming

---

# ▶️ How to Run

## Install Dependencies

```bash
pip install requests
```

Tkinter is included with most standard Python installations.

---

## Run the Application

```bash
python main.py
```

---

# 💡 Engineering Takeaway

The main takeaway from this project was understanding how an existing application can evolve by replacing static data with dynamic data from an external API.

Revisiting the Day 17 project also reinforced the importance of separating responsibilities between the API/data layer, quiz logic, and user interface.

This small upgrade made the application more dynamic while strengthening my understanding of API integration, JSON processing, OOP, and GUI development.

---

# 📈 Challenge Progress

**34/100 Days Completed**

Continuing to revisit Python fundamentals through practical projects while strengthening software engineering and backend development skills.

---

🚀 Revisiting Python Fundamentals | Building Better Software Every Day