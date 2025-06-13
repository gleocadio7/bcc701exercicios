dese = input('Informe se deseja imprimir um retângulo (s/n): ')
if dese == 's':
    while dese == 's':
        alt = int(input('\nInforme a altura do retângulo: '))
        larg = int(input('Informe a largura do retângulo: '))
        
        if alt == 0 or larg == 0 or alt > larg:
            print('Entrada inválida.')
        else:
            for i in range(alt):
                print('')
                for j in range(larg):
                    print('*', end='')
            
            dese = input('\n\nInforme se deseja imprimir outro retângulo (s/n): ')
    