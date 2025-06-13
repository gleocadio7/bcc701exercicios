nome = input('Informe o nome do juiz: ')
part = int(input('Informe a quantidade de partidas: '))

imp=0;fal=0;car=0;acr=0;

for i in range(part):
    print(f'\nPartida {i+1}')
    imp += float(input('. Informe impedimentos.......: '))
    fal += float(input('. Informe faltas.............: '))
    car += float(input('. Informe cartões............: '))
    acr += float(input('. Informe tempo de acréscimo.: '))

print(f'\nEstatísticas do juiz {nome}: ')
print(f'. Impedimentos.......: {imp/part:.2f}.')
print(f'. Faltas.............: {fal/part:.2f}.')
print(f'. Cartões............: {car/part:.2f}.')
print(f'. Tempo de acréscimo.: {acr/part:.2f}.')