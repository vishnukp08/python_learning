a = [1,2,3,6]
b = [2,3,4,5]

a1 = set(a)
b1 = set(b)

common = a1 & b1
union = a1 | b1
diff = b1 - a1

print(f"Common is: {common}\nUnion is: {union}\nDifference is: {diff}")

#print("Common element is: ",a & b)      #Intersection
#print("Union is: ",a | b)