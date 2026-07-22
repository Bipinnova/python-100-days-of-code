# 🐍 Day 21 - Snake Game (Completed) using Python Turtle Graphics

> **Part of my #100DaysOfCode Journey**

This project is part of my journey to **revisit Python fundamentals** by building practical projects while strengthening object-oriented programming and software engineering concepts.

On **Day 20**, I built the foundation of the Snake Game by creating the snake, implementing smooth movement, and adding randomly generated food.

On **Day 21**, I completed the game by implementing snake growth, score tracking, collision detection, and game-over conditions, transforming the project into a fully playable Snake Game.

---

# 🎯 Project Objectives

Through this project, I revisited and strengthened my understanding of:

- Object-Oriented Programming (OOP)
- Classes & Objects
- Inheritance
- Encapsulation
- Modular Programming
- Event-Driven Programming
- Collision Detection
- Game State Management
- Random Number Generation
- Turtle Graphics

---

# 💡 Key Concepts Revisited

## 🐍 Python

- Variables
- Functions
- Lists
- Loops
- Conditional Statements
- Constants
- Modules
- Random Module

---

## 🏗️ Object-Oriented Programming

- Classes & Objects
- Constructors (`__init__`)
- Instance Variables
- Methods
- Encapsulation
- Inheritance
- Object Collaboration

---

## 🖥️ Turtle Graphics

- Turtle Objects
- Screen Object
- Keyboard Events
- Coordinate System
- Animation
- Shape Customization

---

## 🎮 Features Implemented

### ✅ Day 20

- Create the Snake Body
- Smooth Snake Movement
- Random Food Generation

### ✅ Day 21

- Detect Collision with Food
- Snake Growth
- Scoreboard
- Detect Collision with Walls
- Detect Collision with Tail
- Game Over Screen

---

# 📦 Libraries Used

- Turtle
- Random
- Time

---

# 🏗️ Software Engineering Concepts

Although this is a desktop game, it reinforces several important software engineering principles:

- Modular Architecture
- Separation of Responsibilities
- Reusable Components
- State Management
- Event-Driven Programming
- Clean Code Organization
- Object Collaboration

Each responsibility has been separated into its own class:

- **Snake** → Snake movement and growth
- **Food** → Random food generation
- **Scoreboard** → Score management and Game Over message
- **Main** → Game loop and overall application flow

This modular approach makes the project easier to understand, maintain, and extend.

---

# 🚀 Outcome

By completing this project, I strengthened my understanding of object-oriented programming, modular application design, collision detection, and event-driven programming.

This project also demonstrated how multiple independent classes collaborate to build a complete application while keeping the code clean and maintainable.

As part of my **#100DaysOfCode** journey, I continue revisiting Python fundamentals while strengthening the software engineering skills required for backend development using FastAPI.

---

# 📂 Project Structure

```
Day-21-Snake-Game/
│
├── main.py
├── snake.py
├── food.py
├── scoreboard.py
├── README.md
├── requirements.txt
├── output.png
└── demo.mp4 (optional)
```

---

# ▶️ How to Run

### Clone the repository

```bash
git clone https://github.com/Bipinnova/python-100-days-of-code.git
```

### Navigate to the project

```bash
cd Day-21-Snake-Game
```

### Run the project

```bash
python main.py
```

---

# 🎮 Game Features

- Control the snake using the arrow keys.
- Eat food to increase your score.
- Snake grows after eating food.
- Score updates automatically.
- Food appears at random locations.
- Game ends if the snake hits the wall.
- Game ends if the snake collides with its own tail.

---

# 📸 Project Output

The game begins with a three-segment snake controlled by the keyboard.

As the snake eats food, it grows longer and the score increases. The game continues until the snake collides with either the wall or its own body, after which a **GAME OVER** message is displayed.

---

# 📖 What I Reinforced Today

- Object-Oriented Programming
- Inheritance
- Encapsulation
- Modular Programming
- Event Handling
- Collision Detection
- Random Number Generation
- State Management
- Keyboard Events
- Turtle Graphics
- Clean Code Organization

---

# 💡 Engineering Takeaway

Completing the Snake Game highlighted the value of breaking a larger application into smaller, focused components.

Separating movement, food generation, scoring, and collision logic into dedicated classes improved readability, maintainability, and scalability.

These same software engineering principles are widely used in backend systems, where independent modules collaborate to build reliable and maintainable applications.

---

**🚀 Learning in Public | Revisiting Python Fundamentals | Building Better Software Every Day**