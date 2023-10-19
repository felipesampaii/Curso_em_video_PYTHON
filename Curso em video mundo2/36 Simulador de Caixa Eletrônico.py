print('{:=^40}'.format(' Simulador de Caixa Eletrônico '))


valor = int(input('Que valor você quer sacar? R$'))
total = valor
céd = 50
totalcéd = 0
while True:
    if total >= céd:
        total -= céd
        totalcéd += 1
    else:
        if totalcéd > 0:
            print(f'Total de {totalcéd} cédula(s) de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1

        totalcéd = 0
        if céd == 0:
            break
print('Volte sempre!')