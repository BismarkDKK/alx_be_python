# A python program that reminds a user of his or her tasks at hand.


# get user's input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes or no): ")


# processing the task based on priority and time sensitivity
def main():
    match priority:
        case "high":
            string = f"Reminder: '{task}' is a {priority} priority task"
            address(string)
        case "medium":
            string = f"Reminder: '{task}' is a {priority} priority task"
            address(string)
        case "low":
            string = f"Reminder: '{task}' is a {priority} priority task"
            address(string)
        case _:
            no_priority()


# check if the reminder is time-bound and address the user
def address(string):
    if time_bound == "yes":
        print(f"{string} that requires your immediate attention today.")
    elif time_bound == "no":
        print(f"{string}. Consider completing it when you have free time.")
    else:
        print("Incorrect time-bound type selected. Enjoy!")


# function to handle a user typing a different priority
def no_priority():
    print("The priority you typed doesn't exist in the software.")


main()
