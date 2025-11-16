# daily_reminder.py

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match Case for priority messages
match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unrecognized priority level"

# Time sensitivity modification
if time_bound == "yes":
    full_message = f"Reminder: {message} that requires immediate attention today!"
else:
    full_message = f"Note: {message}. Consider completing it when you have free time."

print(full_message)



