print('{:=^40}'.format(' Aprimorando os Dicionários '))

time = list()
jogadores = dict()
partida = list()

while True:
    jogadores.clear()
    jogadores['nome'] = str(input('Nome do jogador: ')).title()
    tot = int(input(f'Quantas partidas {jogadores["nome"]} jogou? '))
    partida.clear()
    for c in range(0, tot):
        partida.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogadores['gols'] = partida[:]
    jogadores['total'] = sum(partida)
    time.append(jogadores.copy())

    resp = str(input('Quer continuar? ')).strip().upper()[0]
    while resp not in 'N':
        print('ERRO! Por favor, dígite apenas S ou N.')
        resp = str(input('Quer continuar? ')).strip().upper()[0]
    if resp in 'N':
        break
print('-' * 50)
print('cod ', end='')
for i in jogadores.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k+1:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 50)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar):  '))
    if busca == 999:
        break
    if  busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
        for i, g  in enumerate(time[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols')
    print('-' * 30)
print('<<< VOLTE SEMPRE >>>')