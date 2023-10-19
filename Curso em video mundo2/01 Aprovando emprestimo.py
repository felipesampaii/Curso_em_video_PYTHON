print('{:=^40}'.format(' Aprovando emprestimo '))


casa = float(input('valor da casa: R$ '))
salario = float(input('Quanto recebe: R$ '))
anos = int(input('Quantos anos de financiamento? '))

minimo = salario * 30 / 100
prestação = casa / (anos * 12)


print('Para pagar uma casa de R${:.2f} em {} anos '. format(casa, anos), end='')
print('a prestação será de R${:.2f}'. format(prestação))
if prestação <= minimo:
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print(f'EMPRÉSTIMO NEGADO!')

print()
print('-' * 40)
input('A perte ENTER para sair')