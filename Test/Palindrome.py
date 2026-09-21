while True:
	text=input("Enter a String(or press q to exit): ")
	if text.lower()=="q":
		break;
	if text==text[::-1]:
		print("Palindrome")
	else:
		print("Not Palindrome")