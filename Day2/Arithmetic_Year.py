"""
from datetime import datetime
current_year=datetime.now().year

year=int(input("Enter year: "))

print("Your age is",current_year-year)
"""
from datetime import datetime

cur_dob=datetime.now().date()

dob=input("Enter your date of birth in YYYYMMDD format: ")

dob_date = datetime.strptime(dob, "%Y%m%d").date()

age = cur_dob.year - dob_date.year

# Check whether the birthday has occurred this year
if (cur_dob.month, cur_dob.day) < (dob_date.month, dob_date.day):
    age -= 1

print("Your age is", age)