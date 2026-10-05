def calc(a,b):
    print(f"Add = {a+b} \nSub = {a-b}\nMul = {a*b}\nDiv = {a/b}\nPower = {a^b}")

while True:
    a=int(input("Enter number: "))
    b=int(input("Enter number: "))
    calc(a,b)