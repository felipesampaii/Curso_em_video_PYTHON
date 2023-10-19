print('======= DESAFIO 11 =======')

l = float(input('Digite a largura da parede: '))
a = float(input('Digite a autura da parde: '))

area = l * a
tinta =  area / 2
print(f'Sua parede tem a dimensao de {l}x{a} e a sua  area é de {area}m².')
print(f'para pintar a parde vc precisara de {tinta:.1f}L.')