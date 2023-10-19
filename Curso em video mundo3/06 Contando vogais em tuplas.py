print('{:=^40}'.format(' Contando vogais em tuplas '))

palavras = ('Teclado', 'Mac', 'Celular', 'Garrafa', 'Jogo', 'Dinheiro',
            'Caneta', 'Caderno', 'Sacola', 'Suporte', 'Livro', 'Curso', 'Python',
            'Programador', 'Aprender', 'Futuro')
for p1 in palavras:
    print(f'\nNa palavra {p1.upper()} temos ', end='')
    for letra in p1:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
