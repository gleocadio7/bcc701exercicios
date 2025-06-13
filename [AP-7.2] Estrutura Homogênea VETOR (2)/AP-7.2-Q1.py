import math
from biblioteca import *
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

print(f'Maior nota: {ma:.1f}')
print(f'Menor nota: {me:.1f}')
print(f'Nota média: {media:.1f}')