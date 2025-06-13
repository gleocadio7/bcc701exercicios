import math
from biblioteca import *

vetor = inputVetor('Informe os nomes dos produtos: ',str)
matriz = inputMatriz('Informe as quantidades de vendas: ',int)

soma = 0;vendas = [];ma = -math.inf;

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        soma += matriz[i][j]
    vendas.append(soma)
    soma = 0

for i in range(len(vendas)):
    if vendas[i] > ma:
        ma = vendas[i]
        gi = i

print(f'Produto selecionado: {vetor[gi]}')
print(f'Total de vendas de {vetor[gi]}: {vendas[gi]}')