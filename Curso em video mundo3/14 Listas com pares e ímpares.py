print('{:=^40}'.format(' Listas com pares e ímpares '))

numeros = [[], []]
valor = 0

for n in range(1, 8):
    valor = int(input(f'Dígite o {n}º valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
print('-' * 20)
numeros[0].sort()
numeros[1].sort()
print(f'Números PARES: {numeros[0]}')
print(f'Números ÍMPARES: {numeros[1]}')
