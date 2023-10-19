print('{:=^40}'.format(' Tabuada v.2.0 '))

num = int(input('Dgite o número que deseja ver a tubuada: '))
for c in range(1, 11):
    print('{} X {:2} = {}'.format(num, c, num*c))