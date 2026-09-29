#take 5 numbers from user, store in list, print:the list, sum, largest
num = []

for i in range(5):
    n = int(input("Enter 5 no.s: \n"))
    num.append(n)

print(num)
print(f"Sum = {sum(num)}")
print(f"Largest = {max(num)}")

#Replace the second item in a list with a new value
n1 = int(input("Enter new number to change 2nd: \n"))
num[1]=n1

print(num)

#Remove the last item from a list
num.pop()
print(num)