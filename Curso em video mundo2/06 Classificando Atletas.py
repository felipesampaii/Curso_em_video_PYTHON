print('{:=^40}'.format(' Classificando Atletas '))

from datetime import date
atual = date.today().year


nasc = int(input('Digite ano de  nascimento: '))
idade = (atual - nasc)

print(f'O atelta tem {idade} anos')
if idade <= 9:
    print('Classificação: MIRIM')

elif idade <= 14:
    print('Classificação: INFANTIL')

elif idade <= 19:
    print('Classificação: JÚNIOR')

elif idade <= 25:
    print('Classificação: SÊNIOR')

else:
    print('Classificação: MASTER')

print()
print('-' * 40)
input('A perte ENTER para sair')