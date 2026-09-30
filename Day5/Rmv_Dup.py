num = [1, 2, 2, 3, 4, 4, 5]

clean = []

for n in num:
    if n not in clean:
        clean.append(n)

print(clean)