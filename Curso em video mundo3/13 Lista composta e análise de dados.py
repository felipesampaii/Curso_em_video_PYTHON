print('{:=^40}'.format(' Lista composta e análise de dados '))

pessoas = list()
dado = list()
maior = menor = 0
while True:
    dado.append(str(input('Nome: ')).capitalize())
    dado.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior  = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado [1] < menor:
            menor = dado[1]
    pessoas.append(dado[:])
    dado.clear()

    resp = str(input('Quer continuar? ')).strip().upper()[0]
    if resp in 'N':
        break
print('-' * 20)
cont = len(pessoas)
print(f'Ao todo, você cadastrou {cont} pessoas')
print(f'O maior peso foi de {maior:.2f}Kg. Peso de ', end='')
for p in pessoas:
   if p[1] == maior:
       print(f'[{p[0]}]', end='')
print('')
print(f'O menor peso foi de {menor:.2f}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
