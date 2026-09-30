'''
square = [x * x for x in range(1,6)]
print(square)

even = [x for x in range(1,11) if x%2 == 0]
print(even)

num = [1,2,3,4,5,6]

res = ["Even" if x%2 ==0 else "Odd" for x in num]
print(res)

'''

square = [x*x for x in range(1,16) if x%2 != 0]
print(square)