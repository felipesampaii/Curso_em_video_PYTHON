print('{:=^40}'.format(' Cadastro de Trabalhador em Python '))

from datetime import datetime

dados = dict()

dados['nome'] = str(input('Nome: ')).title()
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados ['ctps'] != 0:
    dados['Contratação'] = int(input('Ano de Contratação: '))
    dados['slário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['Contratação'] + 35) - datetime.now().year)
print('-' * 30)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')