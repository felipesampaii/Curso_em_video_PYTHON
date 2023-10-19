print('{:=^40}'.format(' Aquele classico da media '))

p1 = float(input('Digite a primeira nota: '))
p2 = float(input('Digite a segunda nota: '))

nota = (p1 + p2) / 2

print(f'Tirando {p1:.1f} e {p2:.1f}, a média do aluno é {nota:.1f}')

if nota < 5.0:
    print('REPROVADO')

elif nota >= 5.0 and nota < 7:
    print('RECUPERAÇÃO')

else:
    print('APROVADO')


print()
print('-' * 40)
input('A perte ENTER para sair')