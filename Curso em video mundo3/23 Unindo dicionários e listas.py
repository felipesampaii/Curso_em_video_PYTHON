print('{:=^40}'.format(' Unindo dicionários e listas '))


galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).title()

    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']

    pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while pessoa['sexo'] not in 'MF':
        print('ERRO! Por favor, dígite apenas M ou F.')
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]

    resp = str(input('Quer continuar? ')).strip().upper()[0]
    while resp not in 'SN':
        print('ERRO! Por favor, dígite apenas S ou N.')
        resp = str(input('Quer continuar? ')).strip().upper()[0]
    galera.append(pessoa.copy())
    if resp in 'N':
        break

print('-=' * 50)
print(f'A) Ao todo temos {len(galera)} pessoas cadrastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2} anos.')
print(f'C) As mulheres cadastradas foram', end='')
for p in galera:
    if p['sexo'] in 'F':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão a cima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<< ENCERRADO >>>')