import math

peso = float(input('Digite seu peso (em kg): '))
altura = float(input('Digite sua altura (em metros): '))
sexo = input('Seu sexo é masculino (M) ou feminino (F)? ')

imc = peso/(math.pow(altura,2))

if sexo == 'M' or sexo == 'F':
    if sexo == 'M':
        if imc > 25:
            pp = 25*(math.pow(altura,2))
            pI = peso - pp
            print(f'Você deve perder {pI:.2f}kg para ter IMC = 25')
        elif imc < 26:
            print('Você não precisa perder peso para ter IMC <= 25')
    else:
        if imc > 24:
            pp = 24*(math.pow(altura,2))
            pI = peso - pp
            print(f'Você deve perder {pI:.2f}kg para ter IMC = 24')
        elif imc < 25:
            print('Você não precisa perder peso para ter IMC <= 24')
else:
    print('A entrada contém dados não reconhecidos') 
    
    