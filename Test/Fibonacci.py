while True:
	n=input("Enter number of terms(or press q to exit): ")
	if n.lower()=="q":
		break
	n=int(n)
	first=0
	second=1
	for i in range(n):
		print(first, end=" ")
		first, second=second, first+second