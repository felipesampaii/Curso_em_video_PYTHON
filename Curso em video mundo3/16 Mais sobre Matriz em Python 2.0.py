print('{:=^40}'.format(' Mais sobre Matriz em Python 2.0 '))

matriz = []
spar = maior = scoluna = 0
for l in range (0, 3):
    linhas = []
    for c in range (0, 3):
        num = int(input(f'Dígite um valor para {c}, {l}: '))
        if num % 2 == 0:
            spar += num
        linhas.append(num)
    matriz.append(linhas)


print('-' * 20)
print('MATRIZ')
for l in range (0, 3):
    linhas = []
    for c in range (0, 3):
        print(f'[{matriz[l] [c]:^5}]', end='')
    print()
print()
print(f'A soma de todos os valores pares é {spar}.')
for l in range(0, 3):
    scoluna += matriz[l][2]
print(f'A soma da terceira coluna é {scoluna}')

for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
            maior = matriz[1][c]
print(f'O maior número da segunda linha é {maior} ')
