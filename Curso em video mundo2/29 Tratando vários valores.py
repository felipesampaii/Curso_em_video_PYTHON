print('{:=^40}'.format(' Tratando vários valores '))

cont = soma = 0
n1 = int(input('Dígite um valor [999 para parar]: '))
while n1 != 999:
    soma += n1
    cont += 1
    n1 = int(input('Dígite um valor [999 para parar]: '))
print(f'Você dígitou {cont} números e a soma entre eles é de {soma}')
