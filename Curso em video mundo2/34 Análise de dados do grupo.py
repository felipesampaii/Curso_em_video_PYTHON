print('{:=^40}'.format(' Análise de dados do grupo '))

i = m = f = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')

    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        i += 1
    if sexo == 'M':
        m += 1
    if sexo == 'F' and idade < 20:
        f += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('')
print('-' * 20)
print(f'Total de pessoas com amis de 18 anos: {i}')
print(f'Ao todo temos {m} homen(s) cadastrado')
print(f'E temos {f} mulher(s) com menos de 20 anos.')
