mora = float(input('Digite a quantidade de Morangos (em kg): '))
maca = float(input('Digite a quantidade de Maçãs (em kg): '))

if mora < 0 or maca < 0:
    print('Entrada inválida')
else:
    if mora < 6:
        mP = mora*2.50
    else:
        mP = mora*2.20
    if maca < 6:
        mM = maca*1.80
    else:
        mM = maca*1.50
    print(f'O valor total da sua compra é R$ {mP+mM:.2f}')