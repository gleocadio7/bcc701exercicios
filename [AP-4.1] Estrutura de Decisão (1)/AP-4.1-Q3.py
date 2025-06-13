import math

lad = int(input('Forneça o tipo de ladrilho (1 ou 2): '))
aSala = int(input('Forneça a área da sala: '))

if lad == 1:
    aLad = 80
else:
    aLad = 60

qtdLad = aSala/aLad

print(f'Quantidade de ladrilhos: {math.ceil(qtdLad)}')