#IanNolon
#5/14/18
#homework1

file = open('engmix.txt')

word = input('Enter a word: ')
for line in file:
    line = line.strip()
    if word == line:
        print(word,'is in the dictionary')
