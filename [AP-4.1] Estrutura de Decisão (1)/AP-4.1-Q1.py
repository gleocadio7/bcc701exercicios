import math

c1 = int(input('Informe o cateto 1 (a): '))
c2 = int(input('Informe o cateto 2 (b): '))
hi = int(input('Informe a hipotenusa (c): '))

c3 = math.pow(c1,2)+math.pow(c2,2)
hip = math.pow(hi,2)

if c3 == hip:
    print(f'{c1}, {c2}, {hi} representam um terno pitagórico')
else:
    print(f'{c1}, {c2}, {hi} NÃO representam um terno pitagórico')