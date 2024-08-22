import math
vIni = int(input('Digite o valor inicial: '))
while vIni < -150 or vIni > 50:
    vIni = int(input('Digite o valor inicial: '))
    
vFin = int(input('Digite o valor final: '))
while vFin <= vIni:
    vFin = int(input('Digite o valor final: '))
    
passo = int(input('Digite o passo: '))
while passo <= 0:
    passo = int(input('Digite o passo: '))
    
for i in range(vIni,vFin+1,passo):
    print()
    for j in range(vIni,vFin+1,passo):
        if i <= 30:
            conta = (i**2)+2*j-3
        elif i <= 60:
            conta = math.sin(0.0175*i)*math.cos(0.0175*j)
        elif i <= 90:
            conta = (1/(i**-2))+j
        else:
            conta = math.pi
        print(f'{conta:10.2f}',end='')
            