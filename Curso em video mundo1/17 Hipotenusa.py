print('======= DESAFIO 17 =======')

from math import sqrt

c = float(input('Comprimento do cateto oposto: '))
s = float(input('Comprimento do cateto adjacente: '))

h = sqrt(c ** 2 + s ** 2)

print(f'A hipotenusa vai medir {h:.2f}')