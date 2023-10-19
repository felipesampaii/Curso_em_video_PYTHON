print('{:=^40}'.format(' Comparando numeros '))


for c in range(0, 20):
    num1 = int(input('Digite um numero inteiro: '))
    num2 = int(input('Digite um outro numero inteiro: '))
    print()

    if num1 > num2:
        print(' O primeiro valor é maior')
        print()

    elif num2 > num1:
        print('O segundo valor é maior')
        print()

    else:
        print('Não existe valor maior, os dois são iguais')
        print()

print('-' * 40)
input('A perte ENTER para sair')