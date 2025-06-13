print('Caixa aberto!\n')
contP = 0;caixa = 'não';pTotal = 0;pPedi=0
while caixa != 'sim':
    qtdP = int(input('Defina a quantidade de itens do pedido: '))
    for i in range(qtdP):
        pItem = float(input(f'. Defina o preço do item {i+1}: '))
        pPedi += pItem
    deli = input('. Defina a cobrança do delivery: ')
    if deli == 'sim':
        pPedi += 15
    print(f'. Valor do pedido: R$ {pPedi:.2f}.')
    contP += 1
    pTotal += pPedi
    pItem = 0
    pPedi = 0
    caixa = input('Defina o fechamento do caixa: ')
    print()
print(f'Caixa fechado!\nNúmero de pedidos: {contP}.\nValor total vendido: R$ {pTotal:.2f}.')
