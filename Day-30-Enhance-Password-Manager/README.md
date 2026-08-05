# 🔐 Day 30 - Password Manager with Search & JSON Storage

> **Part of my #100DaysOfCode Journey**

For Day 30 of my **#100DaysOfCode** challenge, I enhanced the Password Manager by replacing plain text storage with a structured **JSON database** and adding a **Search Password** feature.

The application allows users to generate strong passwords, securely store credentials, search saved accounts, automatically copy passwords to the clipboard, and handle missing or invalid data gracefully.

---

# 🎯 Project Objectives

This project helped me revisit and strengthen my understanding of:

- Tkinter GUI Development
- JSON File Handling
- CRUD-like Data Management
- Password Generation
- Clipboard Integration
- Exception Handling
- Input Validation
- User Experience (UX)

---

# 🛠️ Development Approach

## ✅ Step 1 – Build the User Interface

- Create a clean desktop interface
- Design input forms
- Add action buttons
- Improve usability

**Concepts Revisited**

- Tkinter
- Labels
- Entry Widgets
- Buttons
- Canvas
- Grid Layout

---

## ✅ Step 2 – Generate Secure Passwords

- Random letters
- Random numbers
- Random symbols
- Shuffle password
- Copy password to clipboard

**Concepts Revisited**

- Random Module
- Lists
- List Comprehensions
- String Manipulation

---

## ✅ Step 3 – Store Data in JSON

- Read existing records
- Update with new credentials
- Create JSON file automatically
- Save formatted JSON data

**Concepts Revisited**

- JSON
- Dictionaries
- File Handling

---

## ✅ Step 4 – Search Saved Passwords

- Search by website name
- Display saved email
- Display saved password
- Copy password to clipboard

**Concepts Revisited**

- Dictionary Lookup
- User Interaction
- Clipboard Integration

---

## ✅ Step 5 – Handle Errors

- Missing database
- Invalid JSON
- Empty input fields
- Website not found

**Concepts Revisited**

- Try / Except
- Exception Handling
- Input Validation

---

# 💡 Key Concepts Revisited

## 🐍 Python

- Functions
- Dictionaries
- Lists
- JSON
- File Handling
- Exception Handling
- Random Module

---

## 🖥️ Tkinter

- Labels
- Entry Widgets
- Buttons
- Canvas
- Images
- Grid Layout
- MessageBox

---

## 📂 Data Management

- JSON Read
- JSON Write
- Update Existing Data
- Structured Storage

---

## 💻 Software Engineering

- Clean Code
- Input Validation
- Error Handling
- User Experience
- Data Persistence

---

# 📦 Technologies Used

- Python
- Tkinter
- JSON
- Pyperclip

---

# 🏗️ Project Architecture

### `main.py`

Responsible for:

- Building the GUI
- Generating passwords
- Saving credentials
- Searching passwords
- Reading & Writing JSON
- Input validation
- Clipboard integration

---

# 🚀 Features

- ✅ Secure Password Generator
- ✅ Automatic Clipboard Copy
- ✅ Save Credentials in JSON
- ✅ Search Saved Passwords
- ✅ Email & Password Management
- ✅ Input Validation
- ✅ Exception Handling
- ✅ Professional Desktop GUI

---

# 📂 Project Structure

```text
Day-30-Password-Manager-JSON/
│
├── main.py
├── data.json
├── logo.png
├── README.md
├── requirements.txt
└── output.png
```

---

# ▶️ How to Run

## Install Dependencies

```bash
pip install pyperclip
```

## Run the Application

```bash
python main.py
```

---

# 📖 What I Reinforced Today

- Tkinter GUI Development
- JSON File Handling
- Password Management
- Dictionary Operations
- Exception Handling
- Clipboard Integration
- Input Validation

---

# 💡 Engineering Takeaway

This project reinforced the value of storing application data in a structured format using JSON instead of plain text. Implementing search functionality, input validation, and exception handling improved both the user experience and the maintainability of the application, making it closer to how real-world desktop applications manage persistent data.

---

**🚀 Revisiting Python Fundamentals | Building Better Software Every Day**