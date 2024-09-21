task = input ("Enter your task: ")
# print(task)
priority= input("Priority (high/medium/low): ")
tim= input("Is it time-bound? (yes/no):")

match priority:
  case "high":
    match tim:
      case "yes":
        print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
      case "no":
        print(f"Reminder: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
    
    






