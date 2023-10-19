print('{:=^40}'.format(' Função que descobre o maior '))

def maior(* num):
    cont = maior = 0
    print('-' * 30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor}', end=' ')
        if cont == 0:
            maior = valor
        else:
            if  valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior  valor informado foi {maior}.')
    print('-' * 30)


maior(2, 4 ,8, 1, 3, 6, 7, 9)
maior(23, 545, 213241, 12154654, 123154, 56456447, 145487, 15648)
maior(1, 2, 3)