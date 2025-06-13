nome1 = input('Forneça o nome do candidato 1: ')
n1 = int(input('Forneça o número do candidato 1: '))
nome2 = input('Forneça o nome do candidato 2: ')
n2 = int(input('Forneça o número do candidato 2: '))

ele = int(input('Forneça a quantidade de eleitores: '))
while ele < 3:
    print('A quantidade de eleitores é inferior a 3')
    ele = int(input('Forneça a quantidade de eleitores: '))
c1=0;c2=0;
print('\n## Votação Iniciada')
for i in range(ele):
    voto = int(input('Forneça o número do candidato que deseja votar: '))
    if voto == n1:
        c1+=1
    elif voto == n2:
        c2+=1
if c1 != 0 or c2 !=0:     
    val = ((c1+c2)*100)/ele
    n1p = (c1*100)/(c1+c2)
    n2p = (c2*100)/(c1+c2)
else:
    val = 0
    n1p = 0
    n2p = 0
print('## Votação Encerrada\n')
print(f'Votos válidos: {val:.2f}% ({c1+c2} votos)')
print(f'Votos inválidos: {100-val:.2f}% ({ele-(c1+c2)} votos)')
print(f'Votos para {nome1}: {n1p:.2f}% ({c1} votos)')
print(f'Votos para {nome2}: {n2p:.2f}% ({c2} votos)')

        