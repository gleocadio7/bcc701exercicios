altura = float(input('Digite a altura: '))
sexo = input('Digite o sexo (m ou f): ')

if sexo == 'm':
    pIdeal = (72.7*altura)-58
else:
    pIdeal = (62.1*altura)-44.7
print(f'O peso ideal é {pIdeal:.2f}')