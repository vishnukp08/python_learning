def count_vow():
    txt = input("Enter a string: ")

    vowels = "aeiou"

    count = 0

    for char in txt:
        if txt == vowels:
            count += vowels

count_vow()