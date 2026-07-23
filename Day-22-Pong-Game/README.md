# 🏓 Day 22 - Pong Game using Python Turtle Graphics

> **Part of my #100DaysOfCode Journey**

This project is part of my journey to **revisit Python fundamentals** by building practical projects while strengthening object-oriented programming and software engineering concepts.

For Day 22, I built the classic **Pong Game** using Python's Turtle Graphics module. Instead of trying to build the entire game at once, I approached it by breaking the problem into smaller, manageable tasks and implementing each feature step by step.

This project reinforced concepts such as modular programming, object-oriented design, collision detection, game loops, event handling, and state management.

---

# 🎯 Project Objectives

Through this project, I revisited and strengthened my understanding of:

- Object-Oriented Programming (OOP)
- Classes & Objects
- Inheritance
- Encapsulation
- Modular Programming
- Event Handling
- Collision Detection
- Animation
- Game Loop
- State Management
- Turtle Graphics

---

# 🛠️ Development Approach

To simplify the implementation, I divided the project into the following milestones:

### ✅ Part 1 – Create the Game Screen
- Set up the game window
- Configure screen size and background
- Enable smooth animation using `tracer()`

### ✅ Part 2 – Create and Move the Right Paddle
- Created the right paddle
- Controlled movement using the arrow keys

### ✅ Part 3 – Create the Left Paddle
- Added a second paddle
- Controlled movement using the `W` and `S` keys

### ✅ Part 4 – Create the Ball
- Built the ball as a separate class
- Implemented continuous movement

### ✅ Part 5 – Detect Collision with Walls
- Reversed the ball's direction when it touched the top or bottom wall

### ✅ Part 6 – Detect Collision with Paddles
- Detected paddle collisions
- Changed the ball's direction
- Increased the ball speed after every successful hit

### ✅ Part 7 – Detect When a Paddle Misses
- Reset the ball to the center
- Awarded a point to the opposing player

### ✅ Part 8 – Keep Score
- Created a scoreboard
- Updated scores dynamically
- Displayed scores during gameplay

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

---

## 🏗️ Object-Oriented Programming

- Classes & Objects
- Constructors (`__init__`)
- Instance Variables
- Methods
- Encapsulation
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

## 🎮 Game Development

- Game Loop
- Collision Detection
- Paddle Movement
- Ball Physics
- Score Tracking
- State Management
- Keyboard Controls

---

# 📦 Libraries Used

- Turtle
- Time

---

# 🏗️ Project Architecture

The project is organized into multiple modules, with each class handling a specific responsibility.

### `main.py`
- Controls the main game loop
- Handles keyboard events
- Coordinates all game components
- Detects collisions
- Updates the screen

### `paddle.py`
- Creates the paddles
- Handles paddle movement
- Responds to keyboard input

### `ball.py`
- Controls ball movement
- Detects collisions
- Adjusts ball speed
- Resets the ball after a point is scored

### `scoreboard.py`
- Tracks player scores
- Updates the scoreboard
- Displays scores during gameplay

---

# 🏗️ Software Engineering Concepts

Although Pong is a simple game, it demonstrates several important software engineering principles:

- Breaking large problems into smaller tasks
- Separation of responsibilities
- Modular architecture
- Object collaboration
- Event-driven programming
- Clean and maintainable code
- Incremental development

These same principles are widely used when building scalable backend applications.

---

# 🚀 Outcome

By completing this project, I strengthened my understanding of object-oriented programming, modular design, collision detection, animation, and event-driven programming.

Most importantly, this project reinforced the value of solving complex problems by dividing them into smaller, manageable components before implementing the complete solution.

As part of my **#100DaysOfCode** journey, I continue revisiting Python fundamentals while building a stronger foundation for backend development with FastAPI.

---

# 📂 Project Structure

```text
Day-22-Pong-Game/
│
├── main.py
├── paddle.py
├── ball.py
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
cd Day-22-Pong-Game
```

### Run the project

```bash
python main.py
```

---

# 🎮 Game Features

- Two-player gameplay
- Keyboard-controlled paddles
- Ball movement with increasing speed
- Wall collision detection
- Paddle collision detection
- Automatic score tracking
- Ball reset after scoring
- Continuous gameplay

---

# 📸 Project Output

The game starts with two paddles positioned on opposite sides of the screen.

Players control their paddles using the keyboard while the ball moves across the screen. The ball bounces off walls and paddles, increasing in speed after each successful hit. If a player misses the ball, the opponent earns a point, and the ball resets to the center. The scoreboard updates in real time throughout the game.

---

# 📖 What I Reinforced Today

- Object-Oriented Programming
- Modular Programming
- Event Handling
- Collision Detection
- Game Loop
- Animation
- State Management
- Keyboard Input
- Turtle Graphics
- Clean Code Organization
- Problem Decomposition

---

# 💡 Engineering Takeaway

One of the most valuable lessons from this project was learning to approach complex problems by breaking them into smaller, manageable tasks.

By implementing each feature independently—such as paddle movement, ball behavior, collision detection, and score tracking—I was able to build a complete application in a structured and maintainable way.

This problem-solving approach is equally valuable in backend development, where large systems are designed as a collection of smaller, well-defined components.

---

**🚀 Learning in Public | Revisiting Python Fundamentals | Building Better Software Every Day**