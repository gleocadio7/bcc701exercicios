'''
import math
def calculaComprimento(A,B):
    return math.sqrt(math.pow(B['X']-A['X'],2)+(math.pow(B['Y']-A['Y'],2)))
A = {};B = {}
A['X'] = float(input('Informe a coordenada X de A: '))
A['Y'] = float(input('Informe a coordenada Y de A: '))
B['X'] = float(input('Informe a coordenada X de B: '))
B['Y'] = float(input('Informe a coordenada Y de B: '))
comp = calculaComprimento(A,B)
print(f'\nDistância entre os pontos A e B: {comp:.2f}')
'''
import math
def calculaComprimento(reta):
    return math.sqrt(math.pow(reta['B']['X']-reta['A']['X'],2)+(math.pow(reta['B']['Y']-reta['A']['Y'],2)))
reta = {};A = {};B = {}
A['X'] = float(input('Informe a coordenada X de A: '))
A['Y'] = float(input('Informe a coordenada Y de A: '))
B['X'] = float(input('Informe a coordenada X de B: '))
B['Y'] = float(input('Informe a coordenada Y de B: '))
reta['A'] = A
reta['B'] = B

comp = calculaComprimento(reta)
print(f'\nDistância entre os pontos A e B: {comp:.2f}')