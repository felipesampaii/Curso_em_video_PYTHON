from time import sleep

print('{:=^40}'.format(' Menu de Opçoes '))


num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
player = 0
while player != 5:
    print('=' * 20)
    print('''    [1]SOMAR
    [2]MULTIPLICAR
    [3]MAIOR
    [4]NOVOS NÚMEROS
    [5]SAIR DO PROGRAMA''')
    player = int(input('>>>Qual é a sua opção? '))
    print('=' * 20)

    if player == 1:
        soma = num1 + num2
        print(f'O resultado de {num1} + {num2} = {soma}')

    elif player == 2:
        multiplicar = num1 * num2
        print(f'O resultado de {num1} x {num2} é {multiplicar}')

    elif player == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print(f'Entre {num1} e {num2} o valor maior é {maior}')

    elif player == 4:
        print('Informe os números novamente:')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))

    elif player == 5:
        print('''    Fim do programa
    Muito obrigado!!''')


    else:
        print('Opção inválida. Tente novamente')
    sleep(1)
