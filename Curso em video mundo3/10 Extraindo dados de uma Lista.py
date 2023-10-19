print('{:=^40}'.format(' Extraindo dados de uma Lista '))

num = list()

while True:
    num.append(int(input('Dígite um valor: ')))
    res = str(input('Quer continuar? ')).strip().upper()[0]
    if res in 'N':
        break
num.sort(reverse=True)
print(f'Você dígitou {len(num)} elementos.')
print(f'Os valores em ordem decrescente são {num}')
if 5 in num:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista')
