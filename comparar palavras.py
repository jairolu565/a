from random import shuffle
import os


arquivo = open('arquivo.txt', 'r')
lista = []
for line in arquivo:
    stripped_line = line.strip()
    line_list = stripped_line.split()
    lista.append(line_list)
arquivo.close()

shuffle(lista)

with open('file.txt','w') as file:
    for row in lista:
        s = ''.join(map(str, row))
        file.write(s+'\n')
        print()
