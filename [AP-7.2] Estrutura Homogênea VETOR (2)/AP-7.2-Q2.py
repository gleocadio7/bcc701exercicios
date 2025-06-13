import math
from biblioteca import *
def acimaValor(v,m):
    acima =[]
    for i in range(len(v)):
        if v[i] > m:
            acima.append(i)
    return acima
    
def estatNotas(v):
    ma = -math.inf;me = math.inf;soma =0;
    for i in range(len(v)):
        if v[i] > ma:
            ma = v[i]
        if v[i] < me:
            me = v[i]
        soma+= v[i]
    media = soma/len(v)
    return ma,me,media

v = inputVetor('Digite as notas: ',float)

ma,me,media = estatNotas(v)

vacima = acimaValor(v,media)

print(f'Maior nota: {ma:.1f}')
print(f'Menor nota: {me:.1f}')
print(f'Nota média: {media:.1f}')
print('Notas acima da média: ')
for i in range(len(vacima)):
    print(f' - [{vacima[i]}] = {v[vacima[i]]:.1f}')