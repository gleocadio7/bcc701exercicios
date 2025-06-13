import math
def calculosParede(Lp,Hp):
    Ap = Lp*Hp
    if Ap <= 60000:
        tipo = 'A'
        At = 171
        G = 1000
    elif Ap <=90000:
        tipo = 'B'
        At = 200
        G = 1200
    else:
        tipo = 'C'
        At = 300
        G = 1400
    qtd = Ap/At
    sacos = Ap/G
    return tipo,math.ceil(qtd),math.ceil(sacos)

larg = float(input('Defina a largura da parede (cm): '))
altu = float(input('Defina a altura da parede (cm): '))

while altu > 0 and larg > 0:
    tipo,qtd,sacos=calculosParede(larg,altu)
    print(f'. O tipo de tijolo é: {tipo}')
    print(f'. A quantidade de tijolos é: {qtd}')
    print(f'. A quantidade de argamassa é: {sacos}')
    larg = float(input('\nDefina a largura da parede (cm): '))
    altu = float(input('Defina a altura da parede (cm): '))
    