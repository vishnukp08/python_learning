calc_to_unit=24
units="hours"

def day_to_units(n):
	return f"{n} days are {n * calc_to_unit} {units}"
user=input("Enter no.of days: ")
user=int(user)
res=day_to_units(user)
print(res)