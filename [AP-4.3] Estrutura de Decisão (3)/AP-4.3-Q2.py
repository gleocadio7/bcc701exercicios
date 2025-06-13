mSem = float(input('Forneça a média no semestre: '))
fSem = int(input('Forneça a frequência no semestre: '))

if mSem > 6 and fSem > 74:
    print('Conceito: Aprovado')
else:
    if mSem < 6 and fSem > 74:
        mf = 6 - mSem
        print(f'Conceito: exame especial\nJustificativa: média {mf:.2f} abaixo da mínima')
    else:
        mf = 75-fSem
        print(f'Conceito: reprovado por faltas\nJustificativa: frequência {mf}% abaixo da mínima')
