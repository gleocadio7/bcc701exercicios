from biblioteca import *
print('Loja da tia Maria')
A = inputMatriz('Forneça a matriz de estoque: ',int)
att = int(input('Forneça o número de atualizações: '))
for i in range(att):
    ind = int(input('Forneça o índice da loja: '))
    prod = int(input('Forneça o índice do produto: '))
    nEst = int(input('Forneça o novo estoque: '))
    A[ind][prod] = nEst
    for j in range(len(A)):
        print(A[j])