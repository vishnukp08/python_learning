def add(*args):
    total = 0

    for i in args:
        total = total + i

    return total

print(add(10,20,30))
print(add(10,20,30,90))
print(add(1,2,6,5,8))