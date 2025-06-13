qAp = int(input('Defina a quantidade de apresentações: '))
qJu = int(input('Defina a quantidade de juízes: '))
nota = 0
for i in range(qAp):
    print(f'. Apresentação {i+1}:')
    dif = float(input('  . Defina o grau de dificuldade: '))
    for i2 in range(qJu):
        nota += float(input(f'  . Defina a nota do juíz {i2+1}: '))
    print(f'  . Pontuação da apresentação: {nota*dif:.2f}')
    nota = 0