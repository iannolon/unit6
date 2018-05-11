#IanNolon
#5/11/18
#warmup16.py

file = open('engmix.txt')

count = 0
for line in file:
    line = line.strip()
    if len(line) > 0:
        if line[0] == 'i' and line[-1] == 'n':
            print(line)
            count += 1
print(count)
