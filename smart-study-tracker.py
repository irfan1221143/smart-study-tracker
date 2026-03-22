# Smart Study Tracker CLI
# A beginner-friendly but UNIQUE project
# Tracks study sessions, analyzes productivity, and gives suggestions

import json
import os
from datetime import datetime

DATA_FILE = "study_data.json"

# Load data
def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

# Save data
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Add study session
def add_session():
    subject = input("Enter subject: ")
    duration = int(input("Enter duration (minutes): "))
    mood = input("How was your focus? (good/average/bad): ")

    session = {
        "subject": subject,
        "duration": duration,
        "mood": mood,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    data = load_data()
    data.append(session)
    save_data(data)

    print("Session added successfully!\n")

# View stats
def view_stats():
    data = load_data()

    if not data:
        print("No data available.")
        return

    total_time = sum(session["duration"] for session in data)
    subjects = {}

    for session in data:
        subjects[session["subject"]] = subjects.get(session["subject"], 0) + session["duration"]

    print("\nTotal Study Time:", total_time, "minutes")
    print("Time per subject:")

    for sub, time in subjects.items():
        print(f"  {sub}: {time} minutes")

# Productivity suggestion
def suggestions():
    data = load_data()

    if not data:
        print("No data available.")
        return

    good = sum(1 for s in data if s["mood"] == "good")
    bad = sum(1 for s in data if s["mood"] == "bad")

    print("\nProductivity Insight:")

    if bad > good:
        print("You seem distracted often. Try shorter sessions (25 min - Pomodoro).")
    else:
        print("Good consistency! Try increasing duration gradually.")

# Main menu
def main():
    while True:
        print("\n--- Smart Study Tracker ---")
        print("1. Add Study Session")
        print("2. View Stats")
        print("3. Get Suggestions")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_session()
        elif choice == "2":
            view_stats()
        elif choice == "3":
            suggestions()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
