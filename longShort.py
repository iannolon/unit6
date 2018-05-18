#IanNolon
#5/18/18
#longShort.py - print out the shortest and longest words for each letter in the alphabet

file = open('engmix.txt')

for ch in str('abcdefghijklmnopqurstuvwyxyz'):
    length = 0
    word = ch
    for line in file:
        line = line.split()
        if len(line) > 0:
            if line[0] == ch:
                if len(line) > length:
                    length = len(line)
                    word = line
    print('The shortest word starting with',ch,'is',word,'and it has',length,'letters')
