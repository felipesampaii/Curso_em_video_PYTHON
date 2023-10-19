import utilidades.nome
from utilidades.cursoemvideo.interface import *
from utilidades.cursoemvideo.arquivo import *
from time import sleep

utilidades.nome.exercicio('Criando um menu')

arq = 'cursoemvideo3.txt'

if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadrastadas', 'Cadrastar nova Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        #opção de  listar o conteúdo de um arquivo!
        lerarquivo(arq)

    elif resposta == 2:
        #opção cadrastrar uma nova pessoa
        cabeçalho('NOVO CADRASTRO')
        nome = str(input('Nome: ')).title()
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)

    elif resposta == 3:
        #opção sair do sistema
        cabeçalho('Saindo do sistema... Áté logo!')
        break

    else:
        print('\033[31mERRO! Dígite uma opção válida!\033[m')
    sleep(1)




