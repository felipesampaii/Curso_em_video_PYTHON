print('{:=^40}'.format(' Ficha do Jogador '))

def ficha(jogador='<desconhecido>', gols=0):
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato.')


j = str(input('Jogador: '))
g = str(input('Números de gols?'))
if g.isalnum():
    g = int(g)
else:
    g = 0
if j.strip() == '':
    ficha(gols=g)
else:
    ficha(j, g)