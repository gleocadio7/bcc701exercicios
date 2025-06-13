from biblioteca import *

A = inputMatriz('Informe os resultados do atleta 1: ',int)
B = inputMatriz('Informe os resultados do atleta 2: ',int)

if len(A) != len(B) or len(A[0]) != len(B[0]):
    print('Matrizes incompatíveis.')
else:
    somaA = 0;somaB = 0;empate = 0
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] > B[i][j]:
                somaA += 1
            elif A[i][j] == B[i][j]:
                empate += 1
            else:
                somaB += 1
    print(f'Quantidade de vitórias do atleta 1: {somaA}')
    print(f'Quantidade de vitórias do atleta 2: {somaB}')
    print(f'Quantidade de empates: {empate}')
    
