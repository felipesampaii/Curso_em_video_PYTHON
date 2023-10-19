print('{:=^40}'.format(' Conversor de bases numericas '))

for c in range(0, 20):
    num = int(input('Diigite um numero inteiro: '))
    print('''Escolha uma das bases de conversão
    [1] BINARIO
    [2] OCTAL
    [3]HEXADECIMAL''')
    opcao = int(input('Sua opção: '))

    if opcao == 1:
        binario = bin(num)[2:]
        print(f'O numero {num} convertido para BINARIO é {binario}')
        print()

    elif opcao == 2:
        octal = oct(num)[2:]
        print(f'O numero {num} convertido para OCTAL é {octal}')
        print()

    elif opcao == 3:
        hexadecimal = hex(num)[2:]
        print(f'O numero {num} convertido para HEXADECIMAL é {hexadecimal}')
        print()

    else:
        print('Opção invalida. Tente novamente')
        print()

print('-' * 40)
input('A perte ENTER para sair')

