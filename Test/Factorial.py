while True:
	n=input("Enter a number(or press q to exit): ")
	if n.lower()=="q":
		break;
	n=int(n)
	fact=1
	
	for i in range(1,n+1):
		fact= fact * i

	print(fact)