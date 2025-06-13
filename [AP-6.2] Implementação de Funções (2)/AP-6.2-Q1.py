def ValorProporcional(Q,P):
    V = Q*P/100
    return round(V)

fema = int(input('Informe a quantidade de mulheres: '))
male = int(input('Informe a quantidade de homens: '))

fp = ValorProporcional(fema,20)
mp = ValorProporcional(male,10)

print(f'{fp:.0f} alunas preferem refeição vegetariana.')
print(f'{mp:.0f} alunos preferem refeição vegetariana.')

print(f'A porcentagem de estudantes que preferem refeição vegetariana é {(100*(fp+mp))/(fema+male):.1f}%.')