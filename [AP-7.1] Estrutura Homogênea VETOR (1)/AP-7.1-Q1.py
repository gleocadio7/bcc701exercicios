import math
from biblioteca import *

nome = inputVetor('Digite os nomes dos candidatos: ',str)
qtdV = inputVetor('Digite as quantidades de votos: ',int)
print()
if len(nome) != len(qtdV):
    print('Vetores com tamanhos diferentes')
elif len(nome) < 3:
    print('Quantidade de candidatos insuficiente ')
else:
    ma = -math.inf
    for i in range(len(qtdV)):
        if qtdV[i] > ma:
            ma = qtdV[i]
            maa = i
    print(f'Vencedor das eleições: {nome[maa]}')