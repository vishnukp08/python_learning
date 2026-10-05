def larg(a, b, c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

print(larg(101,25,100))

def huge(a, b, c):
    big = max(a, b, c)
    return big
print(huge(88,45,90))