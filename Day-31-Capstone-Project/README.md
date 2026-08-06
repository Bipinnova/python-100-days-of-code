# 📚 Day 31 - Hindi ↔ English Flash Card App

> **Part of my #100DaysOfCode Journey**

For Day 31 of my **#100DaysOfCode** challenge, I built a **Hindi ↔ English Flash Card Application** using **Python Tkinter**.

This capstone project helps users improve their vocabulary by displaying Hindi words, automatically flipping the card after a few seconds to reveal the English translation, and pronouncing both words using text-to-speech. The application also tracks learning progress by removing mastered words and saving the remaining words for future practice.

---

# 🎯 Project Objectives

This project helped me revisit and strengthen my understanding of:

- Tkinter GUI Development
- CSV Data Processing
- Text-to-Speech Integration
- File Handling
- Data Persistence
- Event-Driven Programming
- State Management
- User Experience (UX)

---

# 🛠️ Development Approach

## ✅ Step 1 – Build the User Interface

- Design the flash card interface
- Display front and back card images
- Add interactive buttons
- Create a clean learning experience

**Concepts Revisited**

- Tkinter
- Canvas
- Labels
- Buttons
- Images
- Grid Layout

---

## ✅ Step 2 – Load Vocabulary Data

- Read vocabulary from CSV
- Convert data into dictionaries
- Load remaining words automatically

**Concepts Revisited**

- Pandas
- CSV Handling
- Dictionaries
- Lists

---

## ✅ Step 3 – Implement Flash Card Logic

- Display random Hindi words
- Automatically flip the card
- Show English translation

**Concepts Revisited**

- Random Module
- Event Scheduling
- Timer Management

---

## ✅ Step 4 – Add Text-to-Speech

- Pronounce Hindi words
- Pronounce English words
- Replay pronunciation using the speaker button

**Concepts Revisited**

- gTTS
- Pygame Mixer
- Audio Playback

---

## ✅ Step 5 – Track Learning Progress

- Mark words as learned
- Remove mastered vocabulary
- Save remaining words automatically

**Concepts Revisited**

- File Handling
- CSV Updates
- Data Persistence

---

# 💡 Key Concepts Revisited

## 🐍 Python

- Functions
- Lists
- Dictionaries
- Random Module
- File Handling
- Exception Handling

---

## 🖥️ Tkinter

- Canvas
- Buttons
- Labels
- Images
- Grid Layout
- Event Handling
- `after()` Scheduling

---

## 📊 Pandas

- Read CSV Files
- Convert DataFrames
- Dictionary Conversion
- Write CSV Files

---

## 🔊 Audio Processing

- Google Text-to-Speech (gTTS)
- Pygame Mixer
- Audio Playback

---

## 💻 Software Engineering

- State Management
- Data Persistence
- Event-Driven Programming
- Clean Code
- User Experience

---

# 📦 Technologies Used

- Python
- Tkinter
- Pandas
- gTTS
- Pygame

---

# 🏗️ Project Architecture

### `main.py`

Responsible for:

- Building the GUI
- Loading vocabulary
- Flash card logic
- Timer management
- Text-to-Speech
- Learning progress tracking

---

# 🚀 Features

- ✅ Hindi ↔ English Flash Cards
- ✅ Automatic Card Flip
- ✅ Hindi Pronunciation
- ✅ English Pronunciation
- ✅ Speaker Button
- ✅ Random Vocabulary
- ✅ Track Learned Words
- ✅ Save Learning Progress
- ✅ Interactive Desktop GUI

---

# 📂 Project Structure

```text
Day-31-Flash-Card-App/
│
├── main.py
├── data/
│   ├── hindi_english.csv
│   └── words_to_learn.csv
├── images/
│   ├── card_front.png
│   ├── card_back.png
│   ├── right.png
│   ├── wrong.png
│   └── speaker.png
├── README.md
├── requirements.txt
└── output.mp4
```

---

# ▶️ How to Run

## Install Dependencies

```bash
pip install pandas pygame gtts
```

## Run the Application

```bash
python main.py
```

---

# 📖 What I Reinforced Today

- Tkinter GUI Development
- CSV File Handling
- Pandas
- Text-to-Speech Integration
- Audio Playback
- Event Scheduling
- State Management
- Data Persistence

---

# 💡 Engineering Takeaway

This capstone project combined GUI development, data processing, text-to-speech, and persistent storage into a practical learning application. Revisiting these concepts reinforced how multiple Python libraries can work together to create an interactive desktop application that delivers a better user experience while maintaining clean and organized code.

---

**🚀 Revisiting Python Fundamentals | Building Better Software Every Day**