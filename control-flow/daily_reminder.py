# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Provide a customized reminder based on priority and time sensitivity
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += ". Consider completing it soon."
    
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
        if time_bound == "yes":
            reminder += " that you should try to finish soon!"
        else:
            reminder += ". You can schedule it for later."
    
    case "low":
        reminder = f"Reminder: '{task}' is a low priority task"
        if time_bound == "yes":
            reminder += " but you might want to get it done today."
        else:
            reminder += ". Consider completing it when you have free time."
    
    case _:
        reminder = "Invalid priority level entered."

# Output the reminder
print(reminder)

