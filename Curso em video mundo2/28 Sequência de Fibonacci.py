print('{:=^40}'.format(' Sequência de Fibonacci '))

n = int(input('Quantos termos você quer mostar? '))
t1 = 0
t2 = 1
print(f'{t1} → {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' → {t3}', end='')
    t1 = t2
    t2 = t3
    cont = cont + 1
print(' → Fim')
