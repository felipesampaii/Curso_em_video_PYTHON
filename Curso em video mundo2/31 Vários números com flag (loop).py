print('{:=^40}'.format(' Vários números com flag '))

soma = cont = 0
while True:
    n1 = int(input('Dígite um valor [909 para parar]: '))
    if n1 == 909:
        break
    cont += 1
    soma += n1
print(f'Você dígitou {cont} números e a soma entre eles é de {soma}')