#IanNolon
#5/10/18
#longestDictionaryWord.py

file = open('engmix.txt')
word = 'a'
for line in file:
    if len(line) > len(word):
        word = line
print(word)