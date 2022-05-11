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

# coding insight
# here "ValueError" is used in the except condition which works for such input programs
# But we can leave only "except:" as it will bypass all the errors, terminate the program and give the message.

# comment
#                      else:
#                          return "you entered a negative value!"
#    is not needed because "else" condition is defined for negative and strings in the
#                         "if num_of_days.isdigit():" condition
#      and
#                           user_input = int(num_for_days)
#    is defined in the "if" condition because otherwise it won't work for the "else" condition
#    if declared in variables in beginning it gets executed before the "if" condition, hence useless!


# WE CAN ALSO USE THE BELOW CODE FOR THE SAME OPERATION WHICH IS EFFICIENT AND WORKS FINE.
# BUT TO SHOW THE EXAMPLE OF NESTED "IF ELSE" WE ARE USING THIS TYPE OF CODE DESIGN.

# def check_point():
#     if num_of_days.isdigit():
#         user_input = int(num_of_days) ending with a proper "else"
#     could have been used instead of "try except" parameter

# def days_to_hours(num_of_days):
#
#     if num_of_days > 0:
#         return f"{num_of_days} days are {num_of_days * to_hours} {hours_unit}"
#     elif num_of_days == 0:
#         return "you entered 0, enter a valid positive number"

# def check_point():
#     if num_of_days.isdigit():
#         user_input = int(num_of_days)
#         my_output = days_to_hours(user_input)
#         print(my_output)
#     else:
#         print("not a valid input for a program designed for integers greater than 0")
# check_point()

# operation
while True:
    num_of_days = input("enter the num of days to be converted into hours :\n ")
    check_point()

# comment
# num_of_days has to be defined inside while condition , if not it will ask for input once and run for the same value
# infinite times
