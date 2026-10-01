txt = "teacher"

count = {}

for ch in txt:
    count[ch] = count.get(ch, 0) + 1

print(count)

high = max(count, key=count.get)
print(f"{high} : {count[high]}")