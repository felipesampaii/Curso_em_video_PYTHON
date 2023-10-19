print('{:=^40}'.format(' Lista de preços com tuplas '))

compras = ('Lápis', 1.75,
           'Borracha', 2,
           'Caderno', 15.90,
           'Estojo', 25,
           'Transferidor', 4.20,
           'Compasso', 9.99,
           'Mochila', 120.32,
           'Canetas', 22.30,
           'Livro', 34.90)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range (0, len(compras)):
    if pos % 2 == 0:
        print(f'{compras[pos]:.<30}', end='')
    else:
        print(f'R${compras[pos]:>7.2f}')
print('-' * 40)