from biblioteca import *
print('Ministério do Meio Ambiente')
V = inputVetor('Informe as metas dos estados: ',int)
A = inputMatriz('Informe o plantio de árvores: ',int)
soma = 0
for i in range(len(A[0])):
    for j in range(len(A)):
        soma+=A[j][i]
    if V[i] > soma:
        print(f'Estado {i+1}, meta = {V[i]}, plantio = {soma}')
    soma = 0