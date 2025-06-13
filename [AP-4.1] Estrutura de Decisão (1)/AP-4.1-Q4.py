nome = input('Entre com o nome: ')
idade = float(input('Entre com a idade: '))
sexo = input('Entre com o sexo (m ou f): ')

if sexo == 'm'  and idade < 18:
    falta = 18 - idade
    print(f'Faltam {falta:.1f} anos para {nome} atingir a maioridade')
elif sexo =='f' and idade < 21:
    falta = 21 - idade
    print(f'Faltam {falta:.1f} anos para {nome} atingir a maioridade')
else:
    print(f'{nome} tem maioridade civil')