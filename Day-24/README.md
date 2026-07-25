# 🐍 Day 24 - Professional Snake Game (Enhanced Version)

> **Part of my #100DaysOfCode Journey**

For Day 24, I enhanced the Snake Game I built earlier by making it more modular and adding new gameplay features. The focus was on improving code organization, game experience, and applying better software engineering practices.

---

# 🎯 Project Objectives

This project helped me strengthen my understanding of:

- Object-Oriented Programming (OOP)
- Modular Programming
- File Handling
- Game Loop
- Collision Detection
- State Management
- Configuration Management
- Code Reusability
- Turtle Graphics

---

# 🛠️ Features Added

Compared to the previous Snake Game, I added:

- ✅ Centralized game settings using `settings.py`
- ✅ High Score persistence using a file (`data.txt`)
- ✅ Dynamic game speed
- ✅ Level system
- ✅ Background music
- ✅ Sound effects for food and game over
- ✅ Improved scoreboard
- ✅ Better project structure
- ✅ Cleaner and reusable code

---

# 💡 Key Concepts Revisited

## 🐍 Python

- File Handling
- Modules
- Functions
- Constants
- Lists
- Loops
- Conditional Statements

---

## 🏗️ Object-Oriented Programming

- Classes & Objects
- Encapsulation
- Object Collaboration
- Modular Design

---

## 🎮 Game Development

- Game Loop
- Collision Detection
- Dynamic Difficulty
- Score Tracking
- Level Progression
- Sound Integration

---

## 💻 Software Engineering

- Separation of Responsibilities
- Modular Architecture
- Configuration Management
- Clean Code
- Maintainable Code
- Code Reusability

---

# 📦 Libraries Used

- Turtle
- Time
- Random
- Pygame

---

# 🏗️ Project Architecture

### `main.py`
Controls the game loop, game flow, collisions, scoring, and speed.

### `snake.py`
Handles snake creation, movement, growth, and direction.

### `food.py`
Generates food at random positions with random colours.

### `scoreboard.py`
Displays score, level, high score, and game messages.

### `settings.py`
Stores all game configuration values in one place.

### `sound.py`
Handles background music and sound effects.

### `data.txt`
Stores the highest score between game sessions.

---

# 🚀 Outcome

This project helped me understand how to improve an existing application by making it more modular, configurable, and maintainable. I also learned how to persist data using file handling and enhance user experience with levels, sounds, and dynamic gameplay.

---

# 📂 Project Structure

```text
Day-24/
│
├── main.py
├── snake.py
├── food.py
├── scoreboard.py
├── settings.py
├── sound.py
├── data.txt
├── assets/
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

- Snake movement
- Food generation
- Snake growth
- Collision detection
- Dynamic speed increase
- Level progression
- High score saving
- Background music
- Sound effects
- Game Over screen

---

# 📖 What I Reinforced Today

- Object-Oriented Programming
- Modular Programming
- File Handling
- Game Loop
- Collision Detection
- State Management
- Configuration Management
- Sound Integration
- Clean Code Organization
- Code Reusability

---

# 💡 Engineering Takeaway

Instead of adding all features directly into a single file, I separated responsibilities across dedicated modules such as `snake.py`, `food.py`, `scoreboard.py`, `settings.py`, and `sound.py`. This made the project easier to understand, maintain, extend, and test. I also learned how file handling can be used to persist data, such as saving the highest score, providing a better user experience across multiple game sessions.

---

**🚀 Learning in Public | Revisiting Python Fundamentals | Building Better Software Every Day**