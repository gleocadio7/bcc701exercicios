cEmp = float(input('Informe o capital emprestado: '))
mQuit = int(input('Informe a quantidade de meses para quitação: '))

if cEmp < 10001 :
    taxa = 0.1
    print('Taxa de juros aplicada: 10%')
else:
    taxa = 0.07
    print('Taxa de juros aplicada: 7%')

juros = cEmp*taxa*mQuit
vTotal = cEmp + juros

print(f'Juros devido: {juros:.2f}')
print(f'Valor total: {vTotal:.2f}')