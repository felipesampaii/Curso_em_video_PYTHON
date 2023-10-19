print('{:=^40}'.format(' Análise de dados em uma tupla '))

num = (int(input('Dígite um valor: ')),
    int(input('Dígite outro valor: ')),
    int(input('Dígite mais um valor: ')),
    int(input('Dígite o último valor: ')))

print('-' * 60)
print(f'Você dígitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição')
else:
    print('O valor 3 não foi dígitado')
print(f'Os valores pares listados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end='  ')

