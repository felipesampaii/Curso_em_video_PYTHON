print('{:=^40}'.format(' Valores únicos em uma Lista '))


num = list()

while True:
    n = int(input('Dígite um valor: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print(f'Esse valor já existe! Digite outro: ')
    r = str(input('Quer continuar [S/N]: ')).strip().upper()[0]

    if r in 'N':
        break
print('-' * 20)
num.sort()
print(f'Você digitou os valores {num}')


