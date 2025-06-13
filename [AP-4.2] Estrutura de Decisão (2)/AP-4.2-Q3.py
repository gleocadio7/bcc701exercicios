import math
qtdL = int(input('Digite a quantidade de lados: '))
if qtdL < 3:
    print('Não é um poligono')
elif qtdL > 6:
    print('Poligono não identificado')
else:
    medida = float(input('Digite a medida do lado: '))
    
    if qtdL == 3:
        area = (math.pow(medida,2)*math.sqrt(3))/4
        tipo = 'triângulo'
        
    elif qtdL == 4:
        area = math.pow(medida,2)
        tipo = 'quadrado'
        
    elif qtdL == 5:
        area = (5*math.pow(medida,2))/(4*math.tan(0.6283))
        tipo = 'pentágono'
        
    else:
        area = (3*math.pow(medida,2)*math.sqrt(3))/2
        tipo = 'hexágono'
        
    print(f'O poligono é um {tipo} com área: {area:.2f}')