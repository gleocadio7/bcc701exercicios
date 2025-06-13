import math
from biblioteca import *
def maioremenor(A):
    ma = -math.inf;me=math.inf

    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] > ma:
                ma = A[i][j]
            if A[i][j] < me:
                me = A[i][j]
    return ma,me
    
A = inputMatriz('Digite a matriz de notas: ',float)

ma,me = maioremenor(A)
print(f'\nMenor nota: {me}')
print('Ocorrências da menor nota:')
for i in range(len(A)):
    for j in range(len(A[0])):
        if A[i][j] == me:
            print(f'. [{i}][{j}]')
print(f'\nMaior nota: {ma}')
print('Ocorrências da maior nota:')
for i in range(len(A)):
    for j in range(len(A[0])):
        if A[i][j] == ma:
            print(f'. [{i}][{j}]')