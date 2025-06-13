from biblioteca import *

def somaMatriz(A,B):
    vetor = [];C = []
    for i in range(len(A)):
        for j in range(len(A[0])):
            temp = A[i][j] + B[i][j]
            vetor.append(temp)       
        C.append(vetor)
        vetor = []
    return C

m1 = inputMatriz('Digite a primeira matriz: ',int)
m2 = inputMatriz('Digite a segunta matriz: ',int)

if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
    print('\nNão é possível somar as matrizes')
else:
    m3 = somaMatriz(m1,m2)
    print(f'\nMatriz resultante:')
    for i in range(len(m3)):
        print(m3[i])