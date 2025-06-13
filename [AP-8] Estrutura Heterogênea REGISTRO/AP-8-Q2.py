def Situacao(V):
    if V['nota'] >= 6:
        return 'APROVADO'
    elif V['nota'] >= 3:
        return 'EXAME ESPECIAL'
    else:
        return 'REPROVADO'
qtdA = int(input('\nDigite a quantidade de alunos: '))
V = []
for i in range(qtdA):
    aux = {}
    nome = input(f'Digite o nome do aluno {i+1}: ')
    nota = float(input(f'Digite a nota do aluno {i+1}: '))
    aux['nome'] = nome
    aux['nota'] = nota
    V.append(aux)
print('Situação dos alunos:')
for i in range(qtdA):
    sit = Situacao(V[i])
    print(f'{i+1}. {V[i]["nome"]} - Nota: {V[i]["nota"]:.2f} - {sit}')