from datetime import datetime

# here we've used only a single module, so we don't have to add daytime.daytime before any parameter.

user_input = input("enter your goal and deadline separated by ':'\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline_date = input_list[1]

deadline_date = datetime.strptime(deadline_date, "%d.%m.%Y")
today_date = datetime.today()
time_till = deadline_date - today_date

# if you don't want to have the time with hours&minutes, then use time_till.days
# ending with "..........{time_till.days} days" as it won't show "days" info.

# if we want to convert the time in hours use the code inside '''...'''
'''hours_till = int(time_till.total_seconds() /60 /60)
print(f"The time remaining for your goal: {goal} is {hours_till} hours")'''

print(f"The time remaining for your goal: {goal} is {time_till}")
# the print command above prints the time remaining with hours&minutes&seconds
