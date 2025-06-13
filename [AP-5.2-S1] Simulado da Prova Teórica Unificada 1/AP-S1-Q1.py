compra = float(input("Defina o valor total da compra: R$ "))
 
if compra < 1:
    print("Erro: Valor total inválido.")
 
else:
    if compra < 251:
        descS = '3'
        descP = 0.03
    elif compra < 551:
        descS = '6'
        descP = 0.06
    elif compra < 751:
        descS = '8'
        descP = 0.08
    else:
        descS = '10'
        descP = 0.1
    print(f'Desconto de {descS}%.')
    print(f'Valor com desconto: R$ {compra-(compra*descP):.2f}')