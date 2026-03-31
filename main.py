# Smart Study Tracker CLI
# Made for tracking daily study habits in a simple way

import json
import os
from datetime import datetime

DATA_FILE = "study_data.json"


# loading previous data if exists
def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        # if file gets corrupted somehow
        print("Data file issue, starting fresh...")
        return []


# saving everything back
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


# taking duration but making sure user doesn't mess up input
def take_duration():
    while True:
        val = input("Duration (in minutes): ").strip()
        if val.isdigit():
            val = int(val)
            if val > 0:
                return val
        print("Enter a valid number bro...")


# simple mood input (keeping it limited for analysis)
def take_mood():
    while True:
        mood = input("Focus level (good/average/bad): ").lower().strip()
        if mood in ["good", "average", "bad"]:
            return mood
        print("Only good / average / bad allowed.")


# adding one study session
def add_session():
    sub = input("Subject name: ").strip()

    if sub == "":
        print("Subject can't be empty.\n")
        return

    dur = take_duration()
    mood = take_mood()

    entry = {
        "subject": sub,
        "duration": dur,
        "mood": mood,
        "time": datetime.now().strftime("%d-%m-%Y %H:%M")
    }

    data = load_data()
    data.append(entry)
    save_data(data)

    print("Saved 👍\n")


# showing stats (basic but useful)
def show_stats():
    data = load_data()

    if len(data) == 0:
        print("No sessions yet.\n")
        return

    total = 0
    subject_map = {}

    for d in data:
        total += d["duration"]

        if d["subject"] not in subject_map:
            subject_map[d["subject"]] = 0

        subject_map[d["subject"]] += d["duration"]

    print("\n--- Stats ---")
    print("Total time:", total, "minutes")
    print("Sessions:", len(data))

    print("Per subject:")
    for s in subject_map:
        print(s, "->", subject_map[s], "min")

    print()


# last few entries (helps to quickly check)
def recent():
    data = load_data()

    if not data:
        print("Nothing to show.\n")
        return

    print("\nLast sessions:")
    for d in data[-5:]:
        print(d["subject"], "|", d["duration"], "min |", d["mood"], "|", d["time"])
    print()


# this part is intentionally simple (not over-smart)
def suggest():
    data = load_data()

    if not data:
        print("No data for suggestion.\n")
        return

    good = 0
    bad = 0
    total = 0

    for d in data:
        total += d["duration"]
        if d["mood"] == "good":
            good += 1
        elif d["mood"] == "bad":
            bad += 1

    avg = total / len(data)

    print("\nSuggestion:")

    # based on focus
    if bad > good:
        print("Focus seems low recently. Maybe reduce distractions.")
    else:
        print("You're doing fine, keep consistency.")

    # based on time
    if avg < 30:
        print("Try increasing session time a bit.")
    elif avg > 90:
        print("Sessions are long, take breaks in between.")
    else:
        print("Study time looks balanced.")

    print()


def main():
    while True:
        print("=== Study Tracker ===")
        print("1. Add")
        print("2. Stats")
        print("3. Recent")
        print("4. Suggestion")
        print("5. Exit")

        ch = input("Choice: ").strip()

        if ch == "1":
            add_session()
        elif ch == "2":
            show_stats()
        elif ch == "3":
            recent()
        elif ch == "4":
            suggest()
        elif ch == "5":
            break
        else:
            print("Wrong input\n")


if __name__ == "__main__":
    main()
