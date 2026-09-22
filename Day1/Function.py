calc_to_unit=24
units="hours"

def day_to_units(n):
	print(f"{n} days are {n * calc_to_unit} {units}")

day_to_units(10)
day_to_units(20)
day_to_units(100)