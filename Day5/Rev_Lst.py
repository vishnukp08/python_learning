#using function

def rev(num):
    for n in range(len(num)-1,-1,-1):
        print(num[n], end = " ")

num = [1, 2, 3, 4, 5]

rev(num)

#print(num[::-1])