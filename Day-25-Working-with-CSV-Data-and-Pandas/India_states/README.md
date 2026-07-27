# 🇮🇳 Day 25 - India States Game

> **Part of my #100DaysOfCode Journey**

For Day 25 of my **#100DaysOfCode** challenge, I built an interactive **India States Game** using **Python Turtle Graphics** and **Pandas**.

The game displays a blank map of India and challenges the player to guess all 29 states. When a correct state name is entered, it appears at its correct location on the map. If the player exits before completing the game, the program automatically generates a CSV file containing all the states that were missed, making it a useful learning tool.

---

# 🎯 Project Objectives

This project helped me strengthen my understanding of:

- Python File Handling
- Pandas DataFrames
- CSV Processing
- Turtle Graphics
- Data Filtering
- User Input Handling
- Interactive Applications

---

# 🛠️ Development Approach

Instead of building everything at once, I divided the project into smaller tasks.

## ✅ Step 1 – Create the Game Window

- Create the Turtle screen
- Load the India map image
- Configure the game window

**Concepts Revisited**

- Turtle Graphics
- Screen Configuration

---

## ✅ Step 2 – Load State Data

- Read the CSV file using Pandas
- Store all state names in a list

**Concepts Revisited**

- Pandas
- DataFrames
- CSV Reading

---

## ✅ Step 3 – Accept User Input

- Display an input dialog
- Read the user's answer
- Format the input correctly

**Concepts Revisited**

- User Input
- String Methods

---

## ✅ Step 4 – Validate the State Name

- Compare the entered state with the available data
- Track correctly guessed states

**Concepts Revisited**

- Lists
- Conditional Statements

---

## ✅ Step 5 – Display Correct Answers

- Find the state's coordinates
- Display the state name on the map

**Concepts Revisited**

- Data Filtering
- Turtle Positioning

---

## ✅ Step 6 – Generate Learning File

- Detect when the player exits
- Identify missing states
- Export them to a CSV file

**Concepts Revisited**

- File Handling
- CSV Writing
- Automation

---

# 💡 Key Concepts Revisited

## 🐍 Python

- Variables
- Lists
- Loops
- Conditional Statements
- Functions
- String Manipulation
- File Handling

---

## 📊 Pandas

- Reading CSV Files
- DataFrames
- Filtering Data
- Exporting CSV Files

---

## 🎮 Turtle Graphics

- Screen Setup
- Display Images
- Turtle Positioning
- Writing Text on Screen

---

## 💻 Software Engineering

- Problem Decomposition
- Modular Programming
- Data-Driven Programming
- Interactive Application Design
- Clean Code

---

# 📦 Libraries Used

- Turtle
- Pandas

---

# 🏗️ Project Architecture

### `main.py`

Responsible for:

- Creating the game window
- Loading state data
- Handling user input
- Displaying guessed states
- Tracking progress
- Generating the learning CSV file

---

# 🚀 Outcome

This project demonstrated how graphical interfaces can be combined with structured data to build an interactive learning application. Using Pandas for data processing and Turtle Graphics for visualization made the project clean, simple, and easy to extend with additional features.

---

# 📂 Project Structure

```text
Day-25-India-States-Game/
│
├── main.py
├── assets/
│   ├── india_blank_map_img.gif
│   ├── india_states.csv
│   └── states_to_learn.csv
├── README.md
└── requirements.txt
```

---

# ▶️ How to Run

```bash
python main.py
```

---

# 🎮 Game Features

- Interactive India map
- Guess all 29 states
- Display correct answers on the map
- Track progress during gameplay
- Automatically generate `states_to_learn.csv`
- Learn missed states after exiting

---

# 📖 What I Reinforced Today

- Pandas DataFrames
- CSV Reading & Writing
- File Handling
- Turtle Graphics
- User Input Handling
- Data Filtering
- Lists & Loops
- Interactive Python Applications

---

# 💡 Engineering Takeaway

This project reinforced how separating **data** from **application logic** makes software easier to build and maintain. By storing state information in a CSV file and using Pandas to process it, the game became flexible and data-driven. It also demonstrated how Python can combine data processing with graphical interfaces to create practical and interactive applications.

---

**🚀 Learning in Public | Revisiting Python Fundamentals | Building Better Software Every Day**