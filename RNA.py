#IanNolon
#5/17/18
#RNA.py

file = open('E_coli_genome.txt')

for line in file:
    line = line.strip()
    print(line.replace('T','U'))
