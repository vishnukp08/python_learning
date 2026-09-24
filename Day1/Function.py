cal_units = 24 * 60 * 60
units = "Seconds"


def calc(n):
    return f"{n} days are {n * cal_units} {units}"


def validate():
    try:
        user_in = int(n)
        if user_in > 0:
            res = calc(user_in)
            print(res)
        elif user_in == 0:
            print("You entered 0")
        else:
            print("You entered negative number")
    except:
        print("Enter valid number")


user = ""

while user.lower() != "exit":
    user = input("Enter no.of days: ")

    # using Split DataType to add items to a list
    print(user.split())
    
    # using SET DataType to avoid duplicate number from the list
    print(set(user.split()))
    
    for n in set(user.split()):
        validate()
