
'''
num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))
num3=int(input("Enter 3rd number: "))


if num1>num2 and num1>num3:
    print(str(num1)+" is Largest.")
    
elif num2>num3 and num2<num1:
    print(str(num2)+" is Largest.")
    
else:
    print(str(num3)+" is Largest.") 


largest=max(num1,num2,num3)
print(str(largest)+" is Largest.")

'''

numbers= []

for i in range(3):
    num=int(input("Enter a number: "))
    numbers.append(num)
    
largest=max(numbers)

print(str(largest)+" is largest.")