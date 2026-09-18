#using if/else
'''
a=int(input("Enter a number: "))

if a%2==0:
    print(str(a)+" is even.")
else:
    print(str(a)+" is odd.")
    
'''

#without using if/else

a=int(input("Enter a number: "))

res={
    0: "Even", 
    1: "Odd"
}

print(res[a%2])