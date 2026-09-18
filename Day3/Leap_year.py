while True:
    year=input("Enter a year(Press q to stop): ")
    if year.lower()=="q":
        break
    year=int(year)

    if year%4==0 and year%100!=0 or year%400==0:
        print(str(year)+" is a Leap year.")
    else:
        print(str(year)+" is not a Leap year.")