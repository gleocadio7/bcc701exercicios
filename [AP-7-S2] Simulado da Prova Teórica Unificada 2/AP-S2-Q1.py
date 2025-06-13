import math
from biblioteca import *
def calculosVetor(v):
    ma = -math.inf;me = math.inf;media = 0
    tam = len(v)
    for i in range(len(v)):
        if v[i] > ma:
            ma = v[i]
        if v[i] < me:
            me = v[i]
        media+=v[i]
    media = round(media/len(v),2)
    return tam,me,ma,media
print('Manipulações de valores de Vetor')
v = inputVetor('Defina o vetor X: ',float)
print('Propriedades do vetor X:')
tam,me,ma,media = calculosVetor(v)
print(f'. Possui {tam} elementos')
print(f'. {me:.2f} é o menor valor')
print(f'. {ma:.2f} é o maior valor')
print(f'. A média dos valores é {media:.2f}')

