print('{:=^40}'.format(' Contagem regressiva '))

from time import sleep

print('Conategm regressiva para estourar os fogos de artificio')
for c in range(10, -1, -1):
    sleep(0.5)
    print(c)
print('BOM! BOM! POooW!')