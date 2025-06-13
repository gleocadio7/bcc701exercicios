nTermos = int(input('Digite o número de termos: '))
raio = int(input('Digite o raio da esfera: '))

pi=0

for i in range(nTermos):
    pi += (((-1)**i)*(4/(2*i+1)))
    
vol = (4/3)*pi*(raio**3)

print(f'pi = {pi:.5f}.\nVolume da esfera = {vol:.5f}.')