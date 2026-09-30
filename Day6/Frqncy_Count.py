#for character in a string
'''
txt = "banana"

count = {}

for ch in txt:
    count[ch] = count.get(ch, 0) + 1

print(count)
'''
#for words in a sentence

txt = "hello python hello word python is great"

count = {}

for word in txt.split():
    count[word] = count.get(word, 0) + 1
print(count)