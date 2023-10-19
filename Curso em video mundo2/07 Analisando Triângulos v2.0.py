print('{:=^40}'.format(' Analisando Triângulos v2.0 '))

r1 = float(input('primeiro segmento: '))
r2 = float(input('Segundo segnmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triangulo!', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ISÓSCELES')
    else:
        print('ESCALENO')
else:
    print('Os segmentos a cima NAO PODEM FORMAT triângulo')

print()
print('-' * 40)
input('A perte ENTER para sair')







