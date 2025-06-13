nFat = int(input('Informe o número que deseja calcular o Fatorial: '))
while nFat < 1:
    nFat = int(input('Número inválido, defina outro: '))
    
q=1;fat=1
while q<nFat+1:
    fat *= q
    q+=1
print(f'O Fatorial de {nFat} é: {fat}')
