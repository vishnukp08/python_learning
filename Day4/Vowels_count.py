txt = input("Enter a word: ")

vow = "a,e,i,o,u"
count = 0

for char in txt:
    if char in vow:
        count += 1
print(f"No.of vowel: {count}")