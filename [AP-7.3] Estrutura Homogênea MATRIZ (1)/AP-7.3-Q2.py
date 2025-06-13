from biblioteca import *

A = inputMatriz('Digite os elementos da matriz: ',int)

if len(A) != len(A[0]):
    print('\nA matriz não é quadrada.')
else:
    print('\nElementos da diagonal principal:')
    for i in range(len(A)):
        if i != len(A)-1:
            print(A[i][i],end=', ')
        else:
            print(A[i][i])

