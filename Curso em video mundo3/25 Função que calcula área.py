print('{:=^40}'.format(' Função que calcula área '))

def área(larg, comp):
    a = larg * comp
    print(f'A área do terro {larg} x {comp} é de {a}m².')


print('Controle de Terrenos')
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)
