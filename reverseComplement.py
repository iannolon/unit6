#IanNolon
#5/17/18
#reverseComplement.py

file = open('E_coli_genome.txt')

#replace T with A, A with T, G with C, and C with G

for line in file:
    line = line.strip()
    line = line.replace('T','T1')
    line = line.replace('A','A1')
    line = line.replace('G','G1')
    line = line.replace('C','C1')
    line = line.replace('T1','A')
    line = line.replace('A1','T')
    line = line.replace('G1','C')
    line = line.replace('C1','G')
    print(line)