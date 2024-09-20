Task = input("Enter your task: ")
Priority = input("Priority (high, medium, low): ").lower()
TimeBound = input("Is it time-bound? (yes,no): ").lower()

match Priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = "Invalid priority level."
if TimeBound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

print(reminder)