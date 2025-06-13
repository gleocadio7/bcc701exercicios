from biblioteca import *
A = inputMatriz('Digite os elementos da matriz: ',int)
col = int(input('\nDigite a coluna que será alterada: '))

while col < 0 or col >= len(A[0]):
    col = int(input('Digite uma coluna válida: '))

print('\nMatriz alterada: ')
for i in range(len(A)):
    A[i][col] = A[i][col]*2
    print(A[i])
    

