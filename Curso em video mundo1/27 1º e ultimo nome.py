nome = str(input('Digite o seu nome: ')).strip().upper().split()
print(f'Seu primeiro nome é {nome [0]}')
print('Seu último nome é {}'.format(nome[len(nome)-1]))
