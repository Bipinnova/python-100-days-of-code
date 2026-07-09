# 🏆 Day 09 - Blind Auction | 100 Days of Python

## 📌 Project Overview

This project is part of my **100 Days of Python Challenge**.

The objective of this project is to build a **Blind Auction System** where multiple participants can place confidential bids, and the program automatically determines the highest bidder.

Although the application is simple, it reinforces several important Python concepts such as dictionaries, functions, loops, user input handling, and decision-making. It also demonstrates how real-world auction systems determine the winning bidder based on submitted bids.

---

## 🎯 Objectives

- Build a console-based Blind Auction application
- Practice working with dictionaries
- Store and retrieve dynamic user data
- Find the highest value from multiple records
- Strengthen problem-solving through real-world logic

---

## 🛠️ Technologies Used

- Python 3

---

## 📚 Concepts Reinforced

- Variables
- User Input (`input()`)
- Dictionaries
- Key-Value Pairs
- Functions
- Function Parameters
- `for` Loops
- Conditional Statements (`if`, `elif`, `else`)
- Dictionary Traversal
- Variables Scope
- f-Strings
- Code Reusability

---

## 💻 Source Code

```python
def find_highest_bidder(bidding_record):

    highest_bid = 0
    winner = ""

    for bidder in bidding_record:

        bid_amount = bidding_record[bidder]

        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ₹{highest_bid}")
```

---

## ▶️ Sample Output

```text
What is your name?: Bipin
What is your bid?: ₹55000

Are there any other bidders?
yes

What is your name?: Rahul
What is your bid?: ₹58500

Are there any other bidders?
yes

What is your name?: Priya
What is your bid?: ₹62000

Are there any other bidders?
no

==================================================
🏆 AUCTION RESULT
==================================================
Winner       : Priya
Winning Bid  : ₹62,000
==================================================
```

---

## 📖 What I Reinforced Today

While building this project, I strengthened my understanding of:

- Working with dictionaries to store dynamic data
- Traversing key-value pairs efficiently
- Finding the highest value from a collection
- Writing reusable functions
- Organizing program logic
- Handling multiple user inputs
- Implementing real-world auction logic

As a Python Backend Developer, revisiting these concepts helps improve logical thinking and strengthens the implementation of business rules, data processing, and backend workflows.

---

## 📂 Project Structure

```text
Day-09-Blind-Auction
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

Although this is a beginner-friendly console application, it reinforces one of the most commonly used data structures in Python—**Dictionaries**.

Dictionaries are extensively used in backend development for storing configurations, processing JSON data, handling API requests, caching, mapping relationships, and implementing business logic.

Revisiting these concepts strengthens problem-solving skills and helps build more efficient and maintainable applications.

---

⭐ Follow my journey as I complete the **100 Days of Python Challenge** while continuously strengthening my Python fundamentals, improving problem-solving skills, and documenting my learning journey in public.