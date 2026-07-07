# 🎯 Day 07 - Hangman | 100 Days of Python

## 📌 Project Overview

This project is part of my **100 Days of Python Challenge**.

The objective of this project is to build a console-based **Hangman Game** where the player guesses a hidden word one letter at a time before running out of lives.

Although this is a classic game, it reinforces several important programming concepts such as loops, conditional statements, lists, string manipulation, randomization, and state management. It also demonstrates how multiple Python modules can work together to build a complete application.

---

## 🎯 Objectives

- Build an interactive console-based game
- Practice random word selection
- Strengthen loop implementation
- Manage game state
- Improve logical thinking through decision-making
- Organize code using multiple Python modules

---

## 🛠️ Technologies Used

- Python 3

---

## 📚 Concepts Reinforced

- Variables
- User Input (`input()`)
- Lists
- String Manipulation
- `for` Loops
- `while` Loops
- Conditional Statements (`if`, `elif`, `else`)
- Membership Operators (`in`, `not in`)
- Random Module (`random.choice()`)
- Module Import
- Game State Management
- Code Organization
- f-Strings

---

## 💻 Source Code

```python
import random

from hangman_words import word_list
from hangman_art import stages, logo

print(logo)

chosen_word = random.choice(word_list)

# Remaining game logic...
```

---

## ▶️ Sample Output

```text
🎯 Welcome to Hangman!

Word to guess:
_ _ _ _ _

****************************6/6 LIVES LEFT****************************

Guess a letter: a

Word to guess:
_ a _ _ _

Guess a letter: z

You guessed z, that's not in the word.
You lose a life.
```

---


## 📖 What I Reinforced Today

While building this project, I strengthened my understanding of:

- Managing application state throughout the game
- Building interactive command-line applications
- Organizing code across multiple Python modules
- Implementing decision-based game logic
- Updating program output dynamically
- Handling repeated user interaction using loops
- Tracking user progress efficiently

As a Python Backend Developer, revisiting these concepts helps improve logical thinking, modular programming, and the ability to design maintainable applications.

---

## 📂 Project Structure

```text
Day-07-Hangman
│
├── README.md
├── main.py
├── hangman_words.py
├── hangman_art.py
├── output.png
├── demo.gif
└── requirements.txt
```

---

## 💡 Engineering Takeaway

Although Hangman is a beginner-friendly game, it reinforces essential software engineering concepts such as state management, modular programming, user interaction, and decision-making.

These principles are widely used in backend development for workflow management, business logic implementation, application state handling, validation, and scalable software design.

---

⭐ Follow my journey as I complete the **100 Days of Python Challenge** while continuously strengthening my Python fundamentals, improving problem-solving skills, and documenting my learning journey in public.