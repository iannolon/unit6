#IanNolon
#5/14/18
#homework2

file = open('engmix.txt')

dictionary = []
for line in file:
    line = line.strip()
    dictionary.append(line)
num = int(input('Enter a number: '))
print(dictionary[num-1])