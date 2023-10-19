print('{:=^40}'.format(' Tuplas com times de futebol '))

serieA = ('América-MG', 'Athletico', 'Atlético-GO', 'Atlético-MG', 'Avaí (subiu da Série B)',
          'Botafogo (subiu da Série B)', 'Bragantino', 'Ceará', 'Corinthians', 'Coritiba (subiu da Série B)', 'Cuiabá',
          'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás (subiu da Série B)', 'Juventude', 'Internacional', 'Palmeiras',
          'Santos', 'São Paulo')


serieB = ('Bahia (caiu da Série A)', 'Brusque', 'Chapecoense', 'CRB', 'Criciúma (subiu da Série C)',
          'Cruzeiro', 'CSA', 'Guarani', 'Grêmio (caiu da Série A)', 'Ituano (subiu da Série C)', 'Londrina',
          'Náutico', 'Novorizontino (subiu da Série C)', 'Operário-PR', 'Ponte Preta', 'Sampaio Corrêa',
          'Sport (caiu da Série A)', 'Tombense (subiu da Série C)', 'Vasco', 'Vila Nova-GO')

print('=' * 20)
print('Times do Brasileirão')
print('=' * 20)

print('Os times da serie A são:')
for time1 in serieA:
    print(f'{time1}')

print('-' * 20)
print('')

print('OS times da serie B são:')
for time2 in serieB:
    print(f'{time2}')
print('-' * 60)
print('')

print(f'Os cincos primeiros time da serie A são: ')
print(f'{serieA[0:5]}')
print('-' * 60)
print('')

print(f'Os cincos primeiros time da serie B são: ')
print(f'{serieB[0:5]}')
print('-' * 60)
print('')

print(f'Os ultimos quatro colocados da serie A são: ')
print(f'{serieA[-4:]}')
print('-' * 60)
print('')

print(f'Os ultimos quatro colocados da serie B são: ')
print(f'{serieB[-4:]}')
print('-' * 60)
print('')

print('Ordem alfabética serie A:')
print(sorted(serieA))
print('')
print('Ordem alfabética serie B:')
print((sorted(serieB)))
print('')

print(f'O Chpecoense esta na {serieB.index("Chapecoense")+1}ª posição')
