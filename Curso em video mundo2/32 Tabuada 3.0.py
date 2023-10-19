print('{:=^40}'.format(' Tabuada 3.0 '))

n = 0

while True:
    print('-' * 50)
    n = int(input('Quer ver a tabuada de qual valor? [Dìgite número negativo para parar]: '))
    if n < 0:
        break
    for c in range (1, 11):
        print(f'{n} x {c} = {n*c}')
print('-' * 50)
print('PROGRAMA TABUADA ENCERRADO.')
