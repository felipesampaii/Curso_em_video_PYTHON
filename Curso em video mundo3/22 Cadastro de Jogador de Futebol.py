print('{:=^40}'.format(' Cadastro de Jogador de Futebol '))

jogadores = dict()
partida = list()


jogadores['nome'] = str(input('Nome do jogador: ')).title()
tot = int(input(f'Quantas partidas {jogadores["nome"]} jogou? '))
for c in range(0, tot):
    partida.append(int(input(f'Quantos gols na partida {c+1}? ')))
jogadores['gols'] = partida[:]
jogadores['total'] = sum(partida)
print('-=' * 30)
print(jogadores)
print('-=' * 30)
for k, v in jogadores.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogadores["nome"]} jogou {len(jogadores["gols"])} partidas')
for i, v in enumerate(jogadores['gols']):
    print((f'    => N partida {i+1}, fez {v} gols'))
print(f'Foi um total de {jogadores["total"]} gols')
