print('{:=^40}'.format(' Função de Contador '))

from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    print('-' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1)


    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.3)
            cont += p
        print('FIM!')
        print()
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.3)
            cont -= p
        print('FIM!')
        print('-' * 20)


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
