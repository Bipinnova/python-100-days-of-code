# 📈 Day 14 - Higher Lower Game | 100 Days of Python

## 📌 Project Overview

This project is part of my **100 Days of Python Challenge**.

The objective of this project is to build a console-based **Higher Lower Game**, where the player compares two entities and predicts which one has a higher popularity score.

For every correct answer, the player's score increases, and the game continues with a new comparison. The game ends when an incorrect prediction is made.

Although this is a simple console application, it reinforces several important programming concepts such as functions, loops, dictionaries, randomization, conditional statements, and game state management.

---

## 🎯 Objectives

- Build an interactive Higher Lower game
- Practice working with dictionaries and lists
- Implement game logic using reusable functions
- Strengthen decision-making through conditional statements
- Manage game state and score throughout the application

---

## 🛠️ Technologies Used

- Python 3

---

## 📚 Concepts Reinforced

- Variables
- User Input (`input()`)
- Functions
- Function Parameters
- Return Statements
- Dictionaries
- Lists
- Random Module (`random.choice()`)
- `while` Loops
- Conditional Statements (`if`, `else`)
- Boolean Logic
- Game State Management
- Code Reusability
- f-Strings

---

## 💻 Source Code

```python
def check_answer(user_guess, a_followers, b_followers):

    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"
```

---

## ▶️ Sample Output

```text
Compare A:
OpenAI, an AI Research Company, from USA.

VS

Against B:
TCS, an Indian IT Services Company, from India.

Who has the higher popularity score?
Type 'A' or 'B': A

You're right!
Current Score: 1
```

---

## 📷 Project Output

Add your project screenshot here.

Example:

![Output](output.png)

---

## 📖 What I Reinforced Today

While building this project, I strengthened my understanding of:

- Working with dictionaries and lists
- Retrieving and formatting structured data
- Implementing reusable functions
- Generating random data for gameplay
- Managing game state and score
- Applying conditional logic for decision-making
- Building interactive command-line applications

As a Python Backend Developer, revisiting these concepts helps improve logical thinking, data handling, modular programming, and the implementation of maintainable business logic.

---

## 📂 Project Structure

```text
Day-14-Higher-Lower
│
├── README.md
├── main.py
├── game_data.py
├── art.py
├── output.png
├── demo.gif
└── requirements.txt
```

---

## 💡 Engineering Takeaway

This project demonstrates how structured data can be combined with reusable functions to build an interactive application.

By separating responsibilities into dedicated functions—such as formatting data, validating user input, and controlling game flow—the code becomes easier to understand, maintain, and extend.

The same design principles are widely used in backend development for processing API responses, implementing business rules, handling user interactions, and building scalable applications.

Revisiting these concepts strengthens problem-solving skills and encourages writing clean, modular, and maintainable Python code.

---

⭐ Follow my journey as I complete the **100 Days of Python Challenge** while continuously strengthening my Python fundamentals, improving problem-solving skills, and documenting my learning journey in public.