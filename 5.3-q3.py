print('Caixa aberto!')
print()
fechamento = 'não';preco = 0;qtdPedidos = 0;vt = 0
while fechamento != 'sim':
    n = int(input('Defina a quantidade de itens do pedido: '))
    for i in range(n):
        preco += float(input(f'. Defina o preço do item {i+1}: '))
    deli = input('. Defina a cobrança do delivery: ')
    if deli == 'sim':
        preco += 15
    print(f'. Valor do pedido: R$ {preco:.2f}.')
    qtdPedidos += 1
    fechamento = input('Defina o fechamento do caixa: ')
    vt += preco
    preco = 0
    print()
print('Caixa fechado!')
print(f'Número de pedidos: {qtdPedidos}.')
print(f'Valor total vendido: R$ {vt:.2f}.')

        