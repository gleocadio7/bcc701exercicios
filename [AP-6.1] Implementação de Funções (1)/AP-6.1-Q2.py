def converteMedidas(M):
    FT = 0.3048*M
    YD = 0.9144*M 
    return (FT,YD )
    
perc = int(input('Digite a quantidade de percursos: '))

for i in range(perc):
    print(f'Percurso {i+1}:')
    tam = float(input('  - Digite o tamanho em metros: '))
    FT,YD = converteMedidas(tam)
    print(f'  - Tamanho em pés...: {FT:.2f}')
    print(f'  - Tamanho em jardas: {YD:.2f}')