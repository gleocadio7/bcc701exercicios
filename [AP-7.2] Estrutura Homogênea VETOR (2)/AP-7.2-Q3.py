import math
from biblioteca import *

def exameEspecial(notas):
    v = []
    for i in range(len(notas)):
        if notas[i] >= 3 and notas[i] < 6:
            v.append(i)
    return v

ma = -math.inf;me = math.inf;media = 0
v = inputVetor('Digite as notas: ',float)
vN = inputVetor('Digite os nomes: ',str)

for i in range(len(v)):
    if v[i] > ma:
        ma = v[i]
    if v[i] < me:
        me = v[i]
    media += v[i]
media = media/len(v)
print(f'Maior nota: {ma:.1f}\nMenor nota: {me:.1f}\nNota média: {media:.1f}')
print('Notas acima da média:')

if len(v)!=1:
    for i in range(len(v)):
        if v[i] >= media:
            print(f' - [{i}] = {v[i]:.1f} ({vN[i]})')
            
print('Notas em Exame Especial:')
vE = exameEspecial(v)
for i in range(len(vE)):
    print(f' - [{vE[i]}] = {v[vE[i]]:.1f} ({vN[vE[i]]})')
    