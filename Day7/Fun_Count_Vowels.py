def count_vow():
    txt = input("Enter a string: ")

    vowels = "aeiou"

    count = 0

    for char in txt.lower():
        if char in vowels:
            count += 1

    return count

print(count_vow())