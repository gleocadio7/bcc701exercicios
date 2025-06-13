import math
n = int(input('Informe a quantidade de experimentos: '))
def variacaoEntropia(ini,fim):
    ini += 273;fim += 273
    ent = 8.314*math.log(fim/ini)
    return ent
for i in range(n):
    print(f'\nExperimento {i+1}: ')
    tINI = float(input('. Informe a temperatura inicial (Celsius): '))
    tFIM = float(input('. Informe a temperatura final (Celsius): '))
    ent = variacaoEntropia(tINI,tFIM)
    print(f'. A variação de entropia é {ent:.3f} J/(mol K)')
    
    
    