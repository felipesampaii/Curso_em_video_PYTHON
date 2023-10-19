print('======= DESAFIO 12 =======')

preço = int(input('Valor do produto: '))

promocao = preço - (preço * 5) / 100
desconto = (preço * 5) / 100

print(f'O valor do produto com 5% de desconto é de R${promocao}')