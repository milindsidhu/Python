# functions


def days_to_units(inputs, conversion_unit):
    if conversion_unit == "hours":
        return f"{inputs} days are {inputs * 24} hours"
    elif conversion_unit == "minutes":
        return f"{inputs} days are {inputs * 24 * 60} minutes"
    else:
        return "Unsupported Unit"

def check_point():
    try:
        user_input = int(days_and_unit_dict["days"])
        if user_input > 0:
            my_output = days_to_units(user_input, days_and_unit_dict["unit"])
            print(my_output)
        elif user_input == 0:
            print("you entered a 0, enter an integer greater than 0")
        else:
            print("Entered a negative number")
    except ValueError:
        print("enter a valid input for a program designed for positive integers greater than 0")


inputs = ""
while inputs != "exit":
    inputs = input("enter the num of days and the unit of conversion separated by ':'\n ")
    days_and_unit = inputs.split(":")
    print(days_and_unit)
    print(type(days_and_unit))
    days_and_unit_dict = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dict)
    print(type(days_and_unit_dict))
    check_point()
