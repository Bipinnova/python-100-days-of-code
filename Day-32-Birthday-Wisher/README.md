# 🎂 Day 32 - Automated Birthday Wisher

> **Part of my #100DaysOfCode Journey**

For Day 32 of my **#100DaysOfCode** challenge, I built an **Automated Birthday Wisher** using **Python**.

The application automatically checks whether today matches a birthday stored in a CSV file. If a match is found, it selects a random birthday letter template, personalizes it by replacing the recipient's name, and sends the birthday wish via email using Gmail SMTP.

---

# 🎯 Project Objectives

This project helped me revisit and strengthen my understanding of:

- Date & Time Handling
- CSV Data Processing
- Email Automation
- File Handling
- Randomization
- SMTP Protocol
- Data Mapping
- Python Automation

---

# 🛠️ Development Approach

## ✅ Step 1 – Read Birthday Data

- Load birthday records from CSV
- Convert data into a dictionary
- Create an efficient lookup structure

**Concepts Revisited**

- Pandas
- CSV File Handling
- Dictionaries

---

## ✅ Step 2 – Check Today's Birthday

- Get the current date
- Compare today's month and day with stored birthdays

**Concepts Revisited**

- datetime Module
- Tuples
- Conditional Statements

---

## ✅ Step 3 – Generate Personalized Letter

- Select a random birthday template
- Replace placeholder with recipient's name

**Concepts Revisited**

- Random Module
- File Handling
- String Manipulation

---

## ✅ Step 4 – Send Birthday Email

- Connect to Gmail SMTP Server
- Authenticate securely
- Send personalized email automatically

**Concepts Revisited**

- SMTP
- Email Automation
- Secure Authentication

---

# 💡 Key Concepts Revisited

## 🐍 Python

- Functions
- Dictionaries
- Tuples
- File Handling
- String Manipulation
- Random Module

---

## 📊 Pandas

- Read CSV Files
- Iterate DataFrames
- Dictionary Conversion

---

## 📅 Date & Time

- datetime Module
- Current Date
- Date Comparison

---

## 📧 Email Automation

- SMTP
- Gmail SMTP Server
- Secure Login
- Send Email

---

## 💻 Software Engineering

- Automation
- Data Processing
- Clean Code
- Reusable Logic

---

# 📦 Technologies Used

- Python
- Pandas
- SMTP (smtplib)

---

# 🏗️ Project Architecture

### `main.py`

Responsible for:

- Loading birthday records
- Checking today's date
- Selecting a random letter template
- Personalizing the message
- Sending birthday emails

---

# 🚀 Features

- ✅ Automatic Birthday Detection
- ✅ Read Birthday Data from CSV
- ✅ Random Birthday Letter Templates
- ✅ Personalized Email Messages
- ✅ Gmail SMTP Integration
- ✅ Automated Email Sending

---

# 📂 Project Structure

```text
Day-32-Automated-Birthday-Wisher/
│
├── main.py
├── birthdays.csv
├── letter_templates/
│   ├── letter_1.txt
│   ├── letter_2.txt
│   └── letter_3.txt
├── README.md
└── output.png
```

---

# ▶️ How to Run

## Install Dependencies

```bash
pip install pandas
```

## Configure Email

Update your Gmail credentials in `main.py`:

```python
MY_EMAIL = "your_email@gmail.com"
MY_PASSWORD = "your_app_password"
```

> **Note:** Use a Gmail **App Password** instead of your account password.

## Run the Application

```bash
python main.py
```

---

# 📖 What I Reinforced Today

- Python Automation
- Pandas
- CSV File Handling
- datetime Module
- SMTP Email Automation
- Random Module
- File Handling

---

# 💡 Engineering Takeaway

This project reinforced how Python can automate repetitive tasks by combining data processing, file handling, date-based logic, and email automation. Building an automated birthday reminder demonstrated how multiple Python modules can work together to create practical real-world automation workflows.

---

**🚀 Revisiting Python Fundamentals | Building Better Software Every Day**