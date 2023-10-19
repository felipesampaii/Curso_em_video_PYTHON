print('{:=^40}'.format(' Jogo do Par ou Ímpar '))

from random import randint

v = 0
while True:
    jogador = int(input('Diga um valor: '))
    pc = randint(0, 11)
    total = jogador + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
    print(f'Você jogou {jogador} e o computador {pc}. total  de {total}', end='')
    print('DEU PAR' if total % 2 == 0 else ' DEU ÍMPAR')

    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break

    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')

print(f'GAME OUVER! Você venceu {v} vezes.')
