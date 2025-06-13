tEmp = float(input('Forneça o capital Total para empréstimo: '))
Emp = float(input('Forneça o capital emprestado: '))

if tEmp < Emp:
    print(f'Empréstimo negado, capital total é de R$ {tEmp:.2f}.')
else:
    while tEmp > Emp:
        mQuit = int(input('Forneça a quantidade de meses para quitação: '))
        if Emp <= 10000 :
            taxa = 0.1
            print('Taxa de juros aplicada: 10%.')
        else:
            taxa = 0.07
            print('Taxa de juros aplicada: 7%.')
    
        juros = Emp*taxa*mQuit
        total = Emp + juros
    
        print(f'Juros devido: {juros:.2f}.')
        print(f'Valor total: {total:.2f}.')
        tEmp = tEmp - Emp
        Emp = float(input('Forneça o capital emprestado: '))
        if tEmp < Emp:
            print(f'Empréstimo negado, capital total é de R$ {tEmp:.2f}.')

    