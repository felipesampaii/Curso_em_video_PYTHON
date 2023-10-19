print('{:=^40}'.format(' Estatísticas em produtos '))

total = mais1k = menor = cont= 0
barato = ' '
while True:
    print('-' * 20)
    produto = str(input('Produto: ')).capitalize()
    preço = float(input('Valor: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        mais1k += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break

print('')
print('-' * 20)
print(f'O total da compra foi R${total:.2f}')
print(f'temos {mais1k} produto que custa mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa {menor:.2f}')
