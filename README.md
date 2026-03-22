# Smart Study Tracker

A command-line based productivity tool that helps students track study sessions, analyze focus levels, and get personalized suggestions for improving consistency.

---

## 📌 Project Overview

The Smart Study Tracker CLI is a command-line based application designed to help students monitor and improve their study habits. It allows users to log study sessions by recording the subject, duration, and focus level. The application stores this data and provides useful insights such as total study time, subject-wise distribution, and basic productivity suggestions based on user performance.

This project focuses on simplicity, usability, and practical learning, making it especially useful for beginners who want to build real-world programming skills while creating a meaningful productivity tool.

---

## 🚀 Features

- Add study sessions with subject, duration, and focus level
- View total study time and subject-wise breakdown
- Get basic productivity insights based on your focus patterns
- Stores data locally using JSON

---

## 🛠️ Tech Stack

- Python 3
- Built-in libraries: `json`, `datetime`, `os`

---

## 📂 Project Structure

smart-study-tracker/
│── main.py
│── study_data.json (auto-created after first run)
│── README.md

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

git clone https://github.com/irfan1221143/smart-study-tracker  
cd smart-study-tracker  

### 2. Install Requirements

No external libraries are required.

Make sure Python is installed:

python --version

---

## ▶️ How to Run

python main.py

---

## 📌 Usage Guide

After running the program, you will see a menu:

1. Add Study Session  
2. View Stats  
3. Get Suggestions  
4. Exit  

### ➤ Add Study Session
- Enter subject name  
- Enter study duration (in minutes)  
- Enter focus level: good, average, or bad  

### ➤ View Stats
- Displays total study time  
- Shows time spent per subject  

### ➤ Get Suggestions
- Provides feedback based on your focus patterns  

---

## 📊 Example Output

Total Study Time: 120 minutes  
Time per subject:  
Math: 60 minutes  
Physics: 60 minutes  

---

## 💡 Future Improvements

- Add graphical visualization of study data  
- Implement streak tracking  
- Export data to CSV  
- Add advanced AI-based recommendations  

---

## 📄 Notes for Evaluators

- The project is fully executable via command line  
- No GUI or external setup is required  
- All data is stored locally in a JSON file  
- Designed with beginner-friendly, clean, and readable code  

---

## 👨‍💻 Author

Submitted by:  
Irfan Alam Ansari  
25BAI11088  
B.Tech in AI & ML  
