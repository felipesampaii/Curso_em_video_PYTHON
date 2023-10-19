salario = float(input('Qual é o salario do colaborador? R$'))
if salario <= 1250.00:
    aumento1 = salario + (salario * 15) / 100
    print(f'Quem ganhava R${salario:.2f} passa a ganhar R${aumento1:.2f}. teve aumento de 15%')
else:
    aumento2 = salario + (salario * 10) / 100
    print(f'Quem ganhava R${salario:.2f} passa a ganhar R${aumento2:.2f}. teve aumento de 10')


