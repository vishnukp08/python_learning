while True:
    text=input("Enter a String(or press q to exit): ")
    if text.lower()=="q":
        break
    print(text[::-1])

