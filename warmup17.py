#IanNolon
#5/17/18
#warmup17.py

file = open('engmix.txt')

for line in file:
    line = line.strip()
    if 'l' in line and 'n' in line and 'i' in line and 'o' in line and 'a' in line:
        print(line)