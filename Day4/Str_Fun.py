text = input("Enter String: ")
t = "hello"

print(len(text))                        #print length
print(text.strip())                     #remove the outer space
print(text.lower())                     #print in lowercase
print(text.upper())                     #print in uppercase
print(t.replace("hello","python"))             #not use for input() type


print("a,b,c".split(","))               
print(text.split(","))

print("-".join(["a","b","c"]))

print("th" in "python")                 #print True
print("th" not in "python")             #print False
print("z" in "python")                  #print False
print("z" not in "python")              #print True