from math import sqrt
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hip = sqrt(pow(co, 2) + pow(ca, 2))
print(f'A hipotenusa vai medir: {hip:.2f} ')