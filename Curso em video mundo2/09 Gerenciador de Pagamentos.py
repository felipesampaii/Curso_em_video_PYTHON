print('{:=^40}'.format(' Gerenciador de Pagamentos '))

preço = float(input('Prço das compras: R$'))

print('''FORMAS DE PAGEMNTO
[1] à vista dinheiro/cheque: 10% de desconto
[2]à vista no cartão: 5% de desconto
[3]em até 2x no cartão: preço formal 
[4]3x ou mais no cartão: 20% de juros''')
opção = int(input('Qual é a opção? '))


if opção == 1:
    promoção = preço - (preço * 10) / 100
    print(f'Sua compra de R${preço:.2f} vai  custa R${promoção:.2f} no final com 10% de desconto.')
elif opção == 2:
    promoção = preço - (preço * 5) / 100
    print(f'Sua compra de R${preço:.2f} vai custa R${promoção:.2f} no final com 10% de desconto.')
elif opção == 3:
    parcela = preço / 2
    print(f'O valor de R${preço:.2f} parcelado em 2x será de R${parcela:.2f}.')
elif preço == 4:
    parcelas = int(input('Quantas parcelas? '))
    juros = preço + (preço * 20) / 100
    final = juros / parcelas
    print(f'Sua compra final de {preço:.2f} parcelado em {parcelas}x com 20% de juros será de {final:.2f}.')
    print(f'Sua compra de {preço:.2f} vai custar R${juros:.2f} no final.')
else:
    total = preço
    print('OPÇÃO INVÁLIDA de pagamento. tente novamente!')


print()
print('-' * 40)
input('A perte ENTER para sair')