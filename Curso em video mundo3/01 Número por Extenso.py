print('{:=^40}'.format(' Número por Extenso '))

n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
     'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Dígite um número entre 0 e 20: '))
    if num == 0 or num <= 20:

        print(f'Você digitou o número {n[num]}')
        print('-' * 20)
        print('Tente novmente.', end='')
    elif num == 999:
        print('-' * 20)
        print('FIM')
        break
