#IanNolon
#5/14/18
#homework4

file = open('engmix.txt')

letter = input('Enter a letter: ')
word = 0
numLetters = 0
for line in file:
    line = line.strip()
    if line.count(letter) > numLetters:
        word = line
        numLetters = line.count(letter)
print(word,'has',numLetters,'occurences of the letter',letter)