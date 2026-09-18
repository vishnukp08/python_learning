while True:
    score=input("Enter your score (Press q to stop): ")
    
    if score.lower()=="q":
        break

    score=int(score)
    if score>=90:
        print("A")
    elif score>=80:
        print("B")
    elif score>=70:
        print("C")
    else:
        print("F")