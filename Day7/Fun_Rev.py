def reverse():
    txt = input("Enter a String: ")

    txt1 = txt.split()

    for i in txt1:
        print(i[::-1], end = " ")
    #for i in range(len(txt1)-1,-1,-1):
        #print(txt1[i][::-1], end= " ")
reverse()