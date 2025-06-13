pInicial = float(input('Informe a posição inicial (Si): '))
while pInicial < 0:
    pInicial = float(input('Informe a posição inicial (Si): '))
    
Vel = float(input('Informe a velocidade (v): '))
while Vel < 1:
    Vel = float(input('Informe a velocidade (v): '))
    
iTempo = float(input('Informe o instante de tempo (t): '))
while iTempo < 1:
    iTempo = float(input('Informe o instante de tempo (t): '))

resul = pInicial+Vel*iTempo

print(f'A posição final no tempo t = {iTempo:.2f} será S = {resul:.2f}')

