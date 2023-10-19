import random

print('{:=^40}'.format(' Jogo de Dados em Python '))

from random import randint
from time import sleep
from operator import itemgetter

jogo = dict()
ranking = list()

for j in range(1, 5):
    jogo[f'jogador{j}'] = randint(1, 6)

print('Valores sorteados:')
for k, v in jogo.items():
    print(f'O {k} tirou {v}')
    sleep(0.5)

print('-' * 30)
ranking = sorted(jogo.items(), key= itemgetter(1), reverse=True)
print('== RANKING DOS JOGAROES ==')
for i, v in enumerate(ranking):
    print(f'{i+1}ª lugar: {v[0]} com {v[1]}')
    sleep(0.5)






