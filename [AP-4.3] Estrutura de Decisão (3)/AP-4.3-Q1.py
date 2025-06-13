mQuat = float(input('Informe a média móvel dos últimos 14 dias: '))
sSeis = int(input('Informe o somatório dos casos dos últimos 6 dias: '))
qHoje = int(input('Informe a quantidade de casos de hoje: '))

dif = ((sSeis+qHoje)/7)-mQuat

taxa = dif/mQuat*100

if taxa < 0:
    print(f'Casos diminuindo em {abs(taxa):.2f}%')
else:
    if taxa < 16:
        print(f'Casos estáveis em {taxa:.2f}%')
    else:
        print(f'Casos aumentando em {taxa:.2f}%')  