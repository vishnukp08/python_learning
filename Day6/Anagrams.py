txt1 = "silent"
txt2 = "listen"

count1 = {}
count2 = {}

for ch in txt1:
    count1[ch] = count1.get(ch, 0) + 1
#print(count1)

for ch in txt2:
    count2[ch] = count2.get(ch, 0) + 1
#print(count2)

if count1 == count2:
    print("Anagrams")
else:
    print("Not Anagrams")

#using sort

if sorted(txt1) == sorted(txt2):
    print("Anagrams")

else:
    print("Not Anagrams")