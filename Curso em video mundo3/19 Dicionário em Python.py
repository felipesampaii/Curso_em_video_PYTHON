print('{:=^40}'.format(' Dicionário em Python '))

aluno = dict()
aluno['nome'] = str(input('Nome: ')).strip().title()
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media']>= 7:
    aluno['situação'] = 'aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-' * 30)
for k, v in aluno.items():
    print(f'- {k} é igual {v}')
