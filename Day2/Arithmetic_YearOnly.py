from datetime import datetime

cur_dob=datetime.now().date()

dob=int(input("Enter your date of birth in YYYYMMDD format: "))

print("Your age is",cur_dob-datetime.strptime(str(dob),"%Y%m%d").date())