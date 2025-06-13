def Somatorio(n):
    s=0
    for i in range(1,n+1):
        s += 1/i
    return s
    
def Produtorio(n):
    p=1
    for i in range(1,n+1):
        p *= 2**(1/i)
    return p

termos = int(input('Defina a quantidade de termos (N): '))
while termos > 0:
    s = Somatorio(termos)
    p = Produtorio(termos)
    print(f'. O valor de S é {s:.3f}')
    print(f'. O valor de P é {p:.3f}')
    termos = int(input('Defina a quatidade de termos (N): '))
    