# 🃏 Day 11 - Blackjack Game | 100 Days of Python

## 📌 Project Overview

This project is part of my **100 Days of Python Challenge**.

The objective of this project is to build a console-based **Blackjack Game** where the player competes against the computer by drawing cards and applying Blackjack rules to achieve the highest score without exceeding 21.

Although this is a beginner-friendly game, it reinforces several important programming concepts such as functions, loops, lists, conditional statements, randomization, and game state management. It also demonstrates how multiple functions can work together to build a complete interactive application.

---

## 🎯 Objectives

- Build an interactive console-based Blackjack game
- Practice modular programming using functions
- Simulate real-world Blackjack rules
- Strengthen logical thinking through decision-making
- Manage application state throughout the game

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
- Lists
- `for` Loops
- `while` Loops
- Conditional Statements (`if`, `elif`, `else`)
- Random Module (`random.choice()`)
- Game State Management
- Code Reusability
- Business Logic Implementation
- f-Strings

---

## 💻 Source Code

```python
def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)
```

---

## ▶️ Sample Output

```text
Do you want to play a game of Blackjack? Type 'y' or 'n': y

Your cards: [10, 7], current score: 17
Computer's first card: 9

Type 'y' to get another card, type 'n' to pass:
n

Your final hand: [10, 7], final score: 17
Computer's final hand: [9, 8], final score: 17

Draw 🙃
```

---

## 📖 What I Reinforced Today

While building this project, I strengthened my understanding of:

- Building interactive command-line applications
- Organizing code into reusable functions
- Managing application state throughout the game
- Implementing game rules using conditional logic
- Simulating random card distribution
- Improving program flow using loops
- Separating business logic into modular functions

As a Python Backend Developer, revisiting these concepts helps improve logical thinking, state management, modular programming, and the implementation of clean, maintainable application logic.

---

## 📂 Project Structure

```text
Day-11-Blackjack
│
├── README.md
├── main.py
├── art.py
├── output.png
├── demo.gif
└── requirements.txt
```

---

## 💡 Engineering Takeaway

Although Blackjack is a console-based game, it reinforces several software engineering principles such as modular programming, state management, reusable functions, and business logic implementation.

The concepts practiced in this project are commonly used in backend development for workflow management, validation, decision-making, rule engines, and interactive applications.

Revisiting these fundamentals helps strengthen problem-solving skills and encourages writing clean, scalable, and maintainable Python code.

---

⭐ Follow my journey as I complete the **100 Days of Python Challenge** while continuously strengthening my Python fundamentals, improving problem-solving skills, and documenting my learning journey in public.