def Relatorio(v,cargo):
    ST=0;TH=0
    for i in range(len(v)):
        if cargo == v[i]['Cargo']:
            ST += v[i]['Salário']
            TH += v[i]['Horas']
        else:
            ST += 0
            TH += 0
    return round(ST,3),TH
v = []
qtd = int(input('Informe a quantidade de funcionários: '))
print('\nEntrada dos funcionários:')
for i in range(qtd):
    aux = {}
    print(f'\nFuncionário {i+1}: ')
    aux['Cargo'] = input('. Informe o Cargo: ')
    aux['Salário'] = float(input('. Informe o Salário: R$ '))
    aux['Horas'] = int(input('. Informe as Horas: '))
    v.append(aux)
print('\nRelatórios:')
carg = input('\nInforme o Cargo: ')
while carg != "":
    ST,TH = Relatorio(v,carg)
    print(f'. Salário Total: R$ {ST:.2f}')
    print(f'. Total de horas: {TH}')
    carg = input('\nInforme o Cargo: ')
