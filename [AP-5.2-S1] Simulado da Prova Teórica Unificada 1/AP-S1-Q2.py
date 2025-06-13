nome = (input('Informe o nome do produto: '))

while  nome != 'fim':
    valor = float(input('Informe o valor do pedido: R$ '))
    if nome == 'Pão de queijo':
        if valor <= 50:
            descP = 0.1
            descS = 10
        elif valor <= 100:
            descP = 0.12
            descS = 12
        else:
            descP = 0.15
            descS = 15
    else:
        if valor <= 50:
            descP = 0.09
            descS = 9
        elif valor <= 100:
            descP = 0.1
            descS = 10
        else:
            descP = 0.11
            descS = 11
    print(f'Percentual de desconto: {descS:.2f}%')
    print(f'Valor com desconto: R$ {valor-(valor*descP):.2f}')
    nome = (input('Informe o nome do produto: '))