num = []

for i in range(5):
    n = int(input("Enter 5 no.s: \n"))
    num.append(n)

print(num)

num.sort()
print(f"\nSorted list is: {num}")