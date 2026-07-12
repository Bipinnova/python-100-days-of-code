# 🎯 Day 12 - Number Guessing Game | 100 Days of Python

## 📌 Project Overview

This project is part of my **100 Days of Python Challenge**.

The objective of this project is to build a console-based **Number Guessing Game** where the player attempts to guess a randomly generated number within a limited number of attempts.

The game provides feedback after each guess, indicating whether the guessed number is too high or too low, helping the player narrow down the correct answer.

Although this is a beginner-friendly project, it reinforces several important programming concepts such as functions, loops, conditional statements, randomization, user interaction, and game state management.

---

## 🎯 Objectives

- Build an interactive console-based game
- Practice random number generation
- Implement different difficulty levels
- Strengthen logical thinking through decision-making
- Improve code organization using reusable functions

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
- Random Module (`random.randint()`)
- `while` Loops
- Conditional Statements (`if`, `elif`, `else`)
- Comparison Operators
- Game State Management
- Code Reusability
- Business Logic Implementation
- f-Strings

---

## 💻 Source Code

```python
def check_answer(user_guess, actual_answer, turns):

    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1

    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1

    else:
        print(f"You got it! The answer was {actual_answer}")
```

---

## ▶️ Sample Output

```text
Welcome to the Number Guessing Game!

I'm thinking of a number between 1 and 100.

Choose a difficulty. Type 'easy' or 'hard':
easy

You have 10 attempts remaining to guess the number.

Make a guess: 50

Too low.

Guess again.

You have 9 attempts remaining to guess the number.

Make a guess: 75

Too high.

Guess again.

...

You got it! The answer was 68
```

---

## 📖 What I Reinforced Today

While building this project, I strengthened my understanding of:

- Breaking application logic into reusable functions
- Managing application state using variables
- Implementing game rules through conditional statements
- Using loops to control program execution
- Working with random number generation
- Providing meaningful feedback to users
- Improving code readability through modular programming

As a Python Backend Developer, revisiting these concepts helps strengthen logical thinking, improve code organization, and build maintainable applications with clear business logic.

---

## 📂 Project Structure

```text
Day-12-Number-Guessing
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

Although this is a simple console-based game, it reinforces important software engineering principles such as modular programming, reusable functions, conditional logic, and application state management.

The project also demonstrates how business rules can be separated into dedicated functions, making the code easier to understand, maintain, and extend.

These concepts are widely used in backend development for implementing validation, workflows, business logic, and user interactions.

Revisiting these fundamentals strengthens problem-solving skills and encourages writing clean, scalable, and maintainable Python applications.

---

⭐ Follow my journey as I complete the **100 Days of Python Challenge** while continuously strengthening my Python fundamentals, improving problem-solving skills, and documenting my learning journey in public.