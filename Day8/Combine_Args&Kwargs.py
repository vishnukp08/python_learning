def details(name, *marks, **info):
    print(f"Name: {name}")

    print("\nMarks: ")
    for i in marks:
        print(i)

    print("\nOther: ")
    for key,value in info.items():
        print(key, ":", value)

details("Vishnu", 85,95,90, sub1 = "Bio", sub2 = "Maths", sub3 = "Physics")
