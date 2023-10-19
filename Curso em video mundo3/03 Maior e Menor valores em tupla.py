print('{:=^40}'.format(' Maior e Menor valores em tupla '))

from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), )
print(f'Sorteei os valores foram: ', end='')

for n in numeros:
    print(f'{n} ', end='')

print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')