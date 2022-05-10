# variables


to_seconds = 24 * 60 * 60
to_minutes = 24 * 60
to_hours = 24
hours_unit = "hours"
seconds_unit = "seconds"
minutes_unit = "minutes"

num_of_days = input("enter the num of days to be converted into hours :\n ")


# functions


def days_to_hours(num_of_days):

    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * to_hours} {hours_unit}"
    elif num_of_days == 0:
        return "you entered 0, enter a valid positive number"


# comment              else:
#                          return "you entered a negative value!"
#    is not needed because "else" condition is defined for negative and strings in the
#                         "if num_of_days.isdigit():" condition

# operations


if num_of_days.isdigit():
    user_input = int(num_of_days)
    my_output = days_to_hours(user_input)
    print(my_output)
else:
    print("not a valid input for a program designed for numbers")
