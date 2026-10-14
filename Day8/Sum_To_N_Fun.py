'''
def sum_to_n(n):
    total = 0

    for i in range(1, n+1):
        total += i

    return total

print(sum_to_n(3))
'''

#using recursion

def sum_to_n(n):
    if n <= 0:
        return 0
    return n + sum_to_n(n-1)

print(sum_to_n(6))