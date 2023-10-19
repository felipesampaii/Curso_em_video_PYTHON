print('{:=^40}'.format(' Maior e Menor valores na Lista '))

mai = 0
men = 0
valores = list()
for c in range(0, 5):
    valores.append(int(input('Dígite um valor: ')))
    if c == 0:
        mai = men = valores[c]
    else:
        if valores[c] > mai:
            mai = valores[c]
        if valores[c] < men:
            men = valores[c]

print('-' * 20)
print(f'Você digitou os valores {valores}')
print(f'O maior valor dígitado foi {mai} nas posições ', end='')
for i, v in enumerate(valores):
    if v == mai:
        print(f'{i}... ', end='')
print()
print(f'O menor valor dígitado foi {men} nas posições ', end='')
for i, v in enumerate(valores):
    if v == men:
        print(f'{i}... ', end='')