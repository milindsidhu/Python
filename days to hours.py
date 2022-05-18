# variables
to_seconds = 24*60*60
to_minutes = 24*60
to_hours = 24
hours_unit = "hours"
seconds_unit = "seconds"
minutes_unit = "minutes"

num_of_days = input("enter the num of days to be converted into hours :\n ")
user_input_hours = int(num_of_days)

# functions

def days_to_hours(num_of_days):
    return f"{num_of_days} days are {num_of_days * to_hours} {hours_unit}"

# operations
my_output = days_to_hours(user_input_hours)
print(my_output)

