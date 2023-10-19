print('======= DESAFIO 13 =======')

salario = float(input('Digite o salario: '))
aumento = int(input('Digite a porcentagem do aumento: '))

ns = salario + (salario * aumento) / 100
aumentoo = (salario * aumento) / 100

print(f'Novo salario é de {ns} \nVocê teve um aumento de {aumentoo}')