#import datetime
from datetime import datetime

user_input = input("Enter goal:date in the format:\n")
input_list = user_input.split(":")

goal = input_list[0]
date_time = input_list[1]

goal = goal.strip()
date_time = date_time.strip()

print(input_list)

#future_date = datetime.datetime.strptime(date_time, "%d.%m.%Y")
future_date = datetime.strptime(date_time, "%d.%m.%Y")
#today_date = datetime.datetime.today()
today_date = datetime.today()

print(f"Entered date: {future_date}")
print(f"Today date: {today_date}")

diff = future_date - today_date
diff = int(diff.total_seconds()/60/60) ##if we need minutes only /60

#print(f"Difference: {diff.days} days")
print(f"Difference: {diff} hours")
