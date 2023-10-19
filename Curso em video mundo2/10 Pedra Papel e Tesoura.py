print('{:=^40}'.format(' GAME: Pedra Papel e Tesoura '))
print()

from random import randint
from time import sleep

opção = ('Pedra', 'Papel', 'tesoura')

pc = randint(0, 2)

print('Vamos jogar jokenpô? ')
resposta = str(input('sim/nao: ').lower())


if resposta == ('sim') or resposta == ('s'):
    for c in range(0, 50):
        print('''Suas opções:
        [ 0 ] PEDRA
        [ 1 ] PAPEL
        [ 2 ] TESOURA''')
        jogador = int(input('Quaç é a sua jogada? '))

        sleep(0)
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PÔ!!!')
        print('-=-' * 20)
        print(f'Computador jogou {opção[pc]}')
        print(f'Jogador Jogou {opção[jogador]}')
        print('-=-' * 20)

        if pc == 0:
            if jogador == 0:
                print('EMPATE!')
                print()
                print('Vamos jogar de novo!')
                print()
            elif jogador == 1:
                print('JOGADOR VENCE!')
                print()
                print('Vamos jogar de novo!')
                print()
            elif jogador == 2:
                print('COMPUTADOR VENCE!')
                print()
                print('Vamos jogar de novo!')
                print()

        elif pc == 1:
            if jogador == 0:
                print('COMPUTADOR VENCE!')
                print()
                print('Vamos jogar de novo!')
                print()
            elif jogador == 1:
                print('EMPATE!')
                print()
                print('Vamos jogar de novo!')
                print()
            elif jogador == 2:
                print('JOGADOR VENCE!')
                print()
                print('Vamos jogar de novo!')
                print()

        elif pc == 2:
            if jogador == 0:
                print('JOGADOR VENCE!')
                print()
                print('Vamos jogar de novo!')
                print()
            elif jogador == 1:
                print('COMPUTADOR VENCE!')
                print()
                print('Vamos jogar de novo!')
                print()
            elif jogador == 2:
                print('EMPATE')
                print()
                print('Vamos jogar de novo!')
                print()


elif resposta == ('não') or resposta == ('n'):
    print('OK! jogamos outra hora.')
else:
    print('OPÇÃO INVALIDA! Tente novamnete.')
