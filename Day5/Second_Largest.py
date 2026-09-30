num = [5,4,2,8,99,100]
'''
num.sort()

print(num[-2])
'''

larg = num[0]
sec_larg = num[0]

for n in num:
    if n > larg:
        sec_larg = larg
        larg = n

    elif n > sec_larg and n != larg:
        sec_larg = n

print(f"Largest: {larg}")
print(f"Second Largest: {sec_larg}")