# variables


to_seconds = 24 * 60 * 60
to_minutes = 24 * 60
to_hours = 24
hours_unit = "hours"
seconds_unit = "seconds"
minutes_unit = "minutes"


# functions


def days_to_hours(num_of_days):
    return f"{num_of_days} days are {num_of_days * to_hours} {hours_unit}"


def check_point():
    try:
        user_input = int(num_of_days)
        if user_input > 0:
            my_output = days_to_hours(user_input)
            print(my_output)
        elif user_input == 0:
            print("you entered a 0, enter an integer greater than 0")
        else:
            print("Entered a negative number")
    except ValueError:
        print("enter a valid input for a program designed for positive integers greater than 0")


num_of_days = ""
while num_of_days != "exit":
    num_of_days = input("enter the num of days to be converted into hours :\n ")
    print(type(num_of_days.split(", ")))
    print(num_of_days.split(", "))
    for num_of_days in num_of_days.split(", "):
        check_point()
