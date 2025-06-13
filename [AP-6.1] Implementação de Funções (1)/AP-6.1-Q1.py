def impostoRenda(b):
    if b <= 1500:
        D = 0
    elif b <= 2500:
        D = 0.05
    elif b <= 4500:
        D = 0.1
    else:
        D = 0.2
    D = b*D
    return D


bruto = float(input('Digite o salário bruto: '))

ir = impostoRenda(bruto)
inss = bruto*0.1
fgts = bruto*0.11

print(f'(-)IR: R$ {ir:.2f}')
print(f'(-)INSS: R$ {inss:.2f}')
print(f'FGTS: R$ {fgts:.2f}')
print(f'Total de descontos: R$ {ir+inss:.2f}')
print(f'Salário Líquido: R$ {bruto-(ir+inss):.2f}')
