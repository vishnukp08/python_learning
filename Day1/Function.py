calc_to_unit=24
units="hours"

def day_to_units(n):
	if n>0:
		return f"{n} days are {n * calc_to_unit} {units}"
	elif n==0:
		return "You entered 0"
	else:
		return "You entered a -ve number"
user=input("Enter no.of days: ")
user=int(user)
res=day_to_units(user)
print(res)