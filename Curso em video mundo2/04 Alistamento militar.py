print('{:=^40}'.format(' Alistamento militar '))


from datetime import date
atual = date.today().year

nasc = int(input('Ano de nascimento: '))
idade = (atual - nasc)

print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')
print()

if idade == 18:
    print('Você tem que se alçistar IMEDIATAMENTE!')

elif idade < 18:
    saldo = 18 - idade
    print(f'ainda faltam {saldo} anos para o alistamento')
    print()
    ano = atual + saldo
    print(f'o seu alistamento será {ano}')

elif idade > 18:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos.')
    print()
    ano = atual - saldo
    print(f'Você deveria ter se alistado em {ano}')


print()
print('-' * 40)
input('A perte ENTER para sair')
