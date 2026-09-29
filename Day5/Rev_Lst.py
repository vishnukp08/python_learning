#using function

def rev(num):
    for i in range(len(num)-1, -1, -1):
        print(num[i],end = " ")

num = [1, 2, 3, 4, 5]

rev(num)

#print(num[::-1])