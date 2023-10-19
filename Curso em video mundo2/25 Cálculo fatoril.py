print('{:=^40}'.format(' Cálculando fatorial '))

n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' X ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1

print(f'{f}')
n = int(input('Digite um número para calcular seu fatorial: '))
print('fim')
