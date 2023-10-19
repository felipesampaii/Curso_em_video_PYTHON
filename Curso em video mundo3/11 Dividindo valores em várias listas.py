print('{:=^40}'.format(' Dividindo valores em várias listas '))

numeros = list()
numpar = list()
numimpar = list()

while True:
    num = int(input('Dígite um valor: '))
    numeros.append(num)

    if num % 2 == 0:
        numpar.append(num)
    else:
        numimpar.append(num)

    resp = str(input('Quer continuar: ')).strip().upper()[0]
    if resp in 'N':
        break

print('-' * 20)
print(f'Os valores digitados são {numeros}')
print(f'Os valores PARES são {numpar}')
print(f'Os valores IMPARES são {numimpar}')