# ☕ Day 15 - Coffee Machine | 100 Days of Python

## 📌 Project Overview

This project is part of my **100 Days of Python Challenge**.

The objective of this project is to build a console-based **Coffee Machine Simulator** that processes customer orders, checks ingredient availability, handles coin-based payments, calculates change, updates inventory, and generates machine reports.

Unlike previous mini-projects, this application combines multiple programming concepts into a single workflow, closely resembling a real-world backend application where business rules, inventory management, payment validation, and resource tracking work together.

---

## 🎯 Objectives

- Build an interactive Coffee Machine application
- Simulate inventory management
- Process customer payments
- Validate available resources
- Calculate and return change
- Track machine profit
- Strengthen modular programming through reusable functions

---

## 🛠️ Technologies Used

- Python 3

---

## 📚 Concepts Reinforced

- Variables
- Dictionaries
- Nested Dictionaries
- User Input (`input()`)
- Functions
- Function Parameters
- Return Statements
- Global Variables
- `while` Loops
- Conditional Statements (`if`, `elif`, `else`)
- Resource Management
- Business Logic Implementation
- Code Reusability
- f-Strings

---

## 💻 Source Code

```python
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_coins():
    total = int(input("How many ₹20 coins?: ")) * 20
    total += int(input("How many ₹10 coins?: ")) * 10
    total += int(input("How many ₹5 coins?: ")) * 5
    total += int(input("How many ₹2 coins?: ")) * 2
    total += int(input("How many ₹1 coins?: ")) * 1

    return total
```

---

## ▶️ Sample Output

```text
What would you like?
(espresso/latte/cappuccino)

latte

Please insert coins.

How many ₹20 coins?: 10
How many ₹10 coins?: 1
How many ₹5 coins?: 0
How many ₹2 coins?: 0
How many ₹1 coins?: 0

Here is ₹10 in change.

☕ Here is your latte. Enjoy!
```

---

## 📖 What I Reinforced Today

While building this project, I strengthened my understanding of:

- Working with nested dictionaries
- Organizing business logic into reusable functions
- Managing application state
- Validating user input and available resources
- Simulating inventory management
- Processing payments and calculating change
- Building interactive command-line applications
- Writing clean and modular Python code

As a Python Backend Developer, revisiting these concepts helps strengthen backend application design, business logic implementation, and writing maintainable software.

---

## 📂 Project Structure

```text
Day-15-Coffee-Machine
│
├── README.md
├── main.py
├── output.png
├── demo.gif
└── requirements.txt
```

---

## 💡 Engineering Takeaway

This project closely resembles the structure of a real-world backend application.

Instead of writing all logic inside a single loop, the application separates responsibilities into dedicated functions such as inventory validation, payment processing, transaction handling, and coffee preparation.

This modular approach improves readability, maintainability, and scalability.

The same design principles are commonly used in backend development for implementing business rules, payment workflows, inventory systems, e-commerce platforms, and REST APIs.

Revisiting these concepts strengthens problem-solving skills and encourages writing clean, modular, and maintainable Python applications.

---

⭐ Follow my journey as I complete the **100 Days of Python Challenge** while continuously strengthening my Python fundamentals, improving problem-solving skills, and documenting my learning journey in public.