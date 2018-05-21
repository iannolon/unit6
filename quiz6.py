#IanNolon
#5/21/18
#quiz6.py

file = open('engmix.txt')

ch = input('Enter a letter: ')

for line in file:
    line = line.strip()
    if ch in line:
        word = []
        for let in line:
            word.append(let)
            if word.count(ch) == 4:
                print(line)

'''
for line in file:
    line = line.strip()
    if len(line) > 8:
        word = []
        for le in line:
            word.append(le)
            if word[0] == word[4] and word[4] == word[8]:
                print(line)
                break
'''

num = int(input('Enter a number: '))
ch2 = input('Enter a letter: ')
goodWord = 0
newWord = False

for line in file:
    line = line.strip()
    if len(line) == num:
        word = []
        for letter in line:
            word.append(letter)
            if word[0] == ch2:
                newWord = True
                goodWord = line
            else:
                newWord = False
                goodWord = 0
        if goodWord != 0 and newWord == True:
            print(goodWord)

newDictionary = []
for line in file:
    line = line.strip()
    if len(line) > 9:
        newDictionary.append(line)
print(newDictionary[7999])


biggestWord = 'a'
mostVowels = 1
for line in file:
    line = line.strip()
    word = []
    for lettr in line:
        word.append(lettr)
    TWVC = 0 #stands for thisWordVowelCount
    TWVC += word.count('a')
    TWVC += word.count('e')
    TWVC += word.count('i')
    TWVC += word.count('o')
    TWVC += word.count('u')
    if TWVC > mostVowels:
        mostVowels = TWVC
        biggestWord = line
print(biggestWord)
