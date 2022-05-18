import datetime

user_input = input("enter your goal and deadline separated by ':'\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline_date = input_list[1]

deadline_date = datetime.datetime.strptime(deadline_date, "%d.%m.%Y")
today_date = datetime.datetime.today()
time_till = deadline_date - today_date
# if you don't want to have the time with hours&minutes, then use time_till.days
# ending with "..........{time_till.days} days" as it won't show "days" info.
print(f"The time remaining for your goal: {goal} is {time_till}")


