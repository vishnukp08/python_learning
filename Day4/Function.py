def calc(n, con_unit):
    if con_unit=="hours": 
        return f"{n} days are {n * 24} hours"
    elif con_unit=="minutes":
        return f"{n} days are {n * 24*60} minutes"
    elif con_unit=="seconds":
        return f"{n} days are {n * 24*60*60} seconds"
    else:
        return "No conversion"


def validate():
    try:
        user_in = int(diction["day"])
        if user_in > 0:
            res = calc(user_in, diction["unit"])
            print(res)
        elif user_in == 0:
            print("You entered 0")
        else:
            print("You entered negative number")
    except:
        print("Enter valid number")


user = ""

while user.lower() != "exit":
    user = input("Enter no.of days and conversion units: \n")

    # check if we entering exit to stop otherwise showing Indexerror
    if user.lower() == "exit":
        break

    # using Split DataType to add items to a list
    day_unit=user.split(":")
    print(day_unit)

    # adding Dictionary to store days and units
    diction={"day":day_unit[0], "unit":day_unit[1]}
    print(diction)
    
    validate()