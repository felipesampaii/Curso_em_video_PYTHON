print('{:=^40}'.format(' Jogo da Adivinhação 2.0 '))

from random import randint
from time import sleep



print('=' * 30)
player = str(input('Vamos jogar? [S/N]:  ')).strip().upper()
print('=' * 30)

while player not in 'Nn':
    pc = randint(0, 10)
    acertou = False
    palpites = 0

    while not acertou:
        jogador = int(input('Qual é seu palpite? '))
        palpites += 1
        if jogador == pc:
            acertou = True
        else:
            if jogador < pc:
                print('Um pouco mais... Tente mais uma vez.')
            elif jogador > pc:
                print('Um pouco menos... Tente mais uma vez.')

    sleep(0.5)
    print(f'Acertou com {palpites} tentativas')
    player = str(input('Quer jogar de novo? [S/N]: '))
    print('=' * 55)
    print('Pensei em outro número de 0 á 10')
