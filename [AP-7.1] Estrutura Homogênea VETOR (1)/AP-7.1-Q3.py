import math
from biblioteca import *
def calculaLucros(vc,lc,vq,lq):
    v=[]
    for i in range(len(vc)):
        v.append(round((vc[i]*lc)+(vq[i]*lq),2))
    return v

vCox = inputVetor('Informe as vendas de coxinhas: ',int)
vQui = inputVetor('Informe as vendas de quibes: ',int)
if len(vCox)!=len(vQui):
    print('Dados de vendas inválidos')
else:
    lCox = float(input('Informe o lucro por unidade de coxinha: R$ '))
    lQui = float(input('Informe o lucro por unidade de quibe: R$ '))
    v = calculaLucros(vCox,lCox,vQui,lQui)
    print(f'Lucros: {v}')
    ma = -math.inf;me = math.inf
    for i in range(len(v)):
        if v[i] > ma:
            ma = v[i]
        if v[i] < me:
            me = v[i]
    print(f'Maior lucro: R$ {ma:.2f}\nMenor lucro: R$ {me:.2f}')