print('{:=^40}'.format(' Índice de Massa Corporal '))

peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))

imc = peso / (altura ** 2)
print(f'O IMC dessa pessoa é de {imc:.2f}')

if imc < 18.5:
    print('Abaixo do Peso')
elif imc >= 18.5 and imc < 25:
    print('Peso Ideal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >= 40:
    print('Obesidade Mórbida')

print()
print('-' * 40)
input('A perte ENTER para sair')