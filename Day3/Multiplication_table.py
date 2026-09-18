 # Print a multiplication table for a number the user inputs (1 to 10)

n=input("Enter a number: ")
n=int(n)

for i in range(1,11):
    print(str(n)+" * "+str(i)+" = "+str(n*i))