stud = {"vishnu":95, "anu":85, "appu":87}

high_stud = max(stud, key=stud.get)

print(f"{high_stud} has highest mark with {stud[high_stud]} marks")