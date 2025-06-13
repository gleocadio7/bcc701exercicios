from biblioteca import *

A = inputMatriz('Digite os elementos da matriz: ',int)
um = 0;resto=0

for i in range(len(A)):
    if A[i][i] != 1:
        um += 1
    for j in range(len(A[0])):
        if i != j:
            if A[i][j] != 0:
                resto += 1
if um == 0 and resto == 0:
    print('A matriz é identidade.')
else:
    print('A matriz não é identidade.')
