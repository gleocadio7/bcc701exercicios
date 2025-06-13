from biblioteca import *
def getDivisores(n):
    v = []
    for i in range(1,n+1):
        if n%i == 0:
            v.append(i)
    return v

q=0
v = inputVetor('Digite os números: ',int)
print()
if len(v)==0:
    print('Nenhum número informado') 
else:
    for i in range(len(v)):
        print()
        for j in range(1,v[i]+1):
            if v[i]%j == 0:
                q+=1
        if q == 2:
            print(f'{v[i]} é um número primo.')
        else:
            divi = getDivisores(v[i])
            
            print(f'{v[i]} não é um número primo.')
            print(f'Seus divisores são:\n{divi}')
        q=0