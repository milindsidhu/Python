# variables
to_seconds = 24 * 60 * 60
to_minutes = 24 * 60
to_hours = 24
hours_unit = "hours"
seconds_unit = "seconds"
minutes_unit = "minutes"

num_of_days_minutes = input("enter the num of days to be converted into minutes :\n ")
user_input_minutes = int(num_of_days_minutes)

num_of_days_hours = input("enter the num of days to be converted into hours :\n ")
user_input_hours = int(num_of_days_hours)

num_of_days_seconds = input("enter the num of days to be converted into seconds :\n ")
user_input_seconds = int(num_of_days_seconds)


# functions


def days_to_hours(num_of_days_hours):
    print(f"{num_of_days_hours} days are {num_of_days_hours * to_hours} {hours_unit}")


def days_to_seconds(num_of_days_seconds):
    print(f"{num_of_days_seconds} days are {num_of_days_seconds * to_seconds} {seconds_unit}")


def days_to_minutes(num_of_days_minutes):
    print(f"{num_of_days_minutes} days are {num_of_days_minutes * to_minutes} {minutes_unit}")


# operations

days_to_hours(user_input_hours)
days_to_minutes(user_input_minutes)
days_to_seconds(user_input_seconds)
