from random import randint
from time import sleep

for c in range(0, 11):
    pc = randint(0, 5)

    print('-=-' * 20)
    print('Vou pensar em um numero entre 0 e 5, tente adivinhar...')
    print('-=-' * 20)


    jogador = int(input('Em que numero eu pensei? '))
    print('PROCESSANDO...')
    sleep(1)
    if jogador == pc:
        print('Parabens! Você conseguiu vencer')
        print()
        print()
        print()

    else:
        print(f'Ganhei! eu pensei no numero {pc} e nao no numero {jogador}')

        print()
        print()
        print()
