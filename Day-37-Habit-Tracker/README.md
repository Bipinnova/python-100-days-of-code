🚀 Day 37 — Habit Tracker API | 100 Days of Coding

Welcome to Day 37 of my #100DaysOfCode journey.

Today, I built a Habit Tracker REST API focused on real-world backend development using Python and FastAPI.

🎯 What I Built

A backend where users can:

🔐 Register and login securely
📋 Create and manage multiple habits
📅 Track daily habit progress
📊 View habit statistics and dashboards
🟩 Synchronize habit records with Pixela
👤 Access only their own habits and records
🛠️ Technologies Used
🐍 Python
⚡ FastAPI
🗄️ PostgreSQL
🔗 SQLAlchemy
🛠️ Alembic
🔐 JWT Authentication & Authorization
🔒 Argon2 Password Hashing
🟩 Pixela API
📦 Pydantic
🌐 REST API
🔄 How It Works
User
 ↓
JWT Authentication
 ↓
Create Habit
 ↓
PostgreSQL
 +
Pixela Graph
 ↓
Daily Habit Record
 ↓
PostgreSQL Record
 +
Pixela Pixel
 ↓
Analytics
 ↓
Habit Dashboard
📊 Database Structure
Users
  │
  └── Habits
        │
        └── Habit Records

PostgreSQL stores the application's users, habits, and daily progress.

🟩 Pixela Integration

Each habit gets its own Pixela graph.

For example:

Coding Practice
      ↓
Pixela Graph
      ↓
Daily Progress Pixels

This allows the habit progress to be visualized using Pixela's contribution-style graph.

📈 Analytics

The project also provides habit analytics such as:

Today's Progress
Total Progress
Maximum
Minimum
Average
Total Days
Streak

and combines the data into dashboard responses.

🔐 Security

Passwords are not stored as plain text.

They are securely hashed using Argon2id, while JWT tokens are used to protect authenticated endpoints.

📚 What I Learned

This project helped me practice:

REST API design
FastAPI project architecture
JWT authentication & authorization
Secure password hashing
PostgreSQL relationships
SQLAlchemy ORM
Alembic migrations
CRUD operations
External API integration
Data synchronization
Analytics and dashboard APIs
🚀 Day 37 Progress

Project: Habit Tracker API
Day: 37/100
Focus: Backend Development + API Integration

Building one project every day, learning by doing, and documenting the journey. 🚀

#️⃣ Hashtags

#100DaysOfCode #Python #FastAPI #PostgreSQL #SQLAlchemy #BackendDevelopment #RESTAPI #JWT #LearningInPublic