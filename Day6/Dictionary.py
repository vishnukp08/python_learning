student = {"name":"Vishnu", "age":24, "course":"CSE"}

print(student)
print(student["name"])

for key, value in student.items():
    print(f"{key} : {value}")

student["college"] = "GCEK"
print(student)

student["age"] = 25
print("\n",student)

for key,value in student.items():
    print(f"{key} : {value}")

student.pop("age")
print("\n",student)

#del student["age"]

for key, value in student.items():
    print(f"{key} : {value}")