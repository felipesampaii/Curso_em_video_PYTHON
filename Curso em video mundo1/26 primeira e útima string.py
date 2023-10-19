frase = str(input('Digite uma frase ou nome: ')).strip().upper()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primiera letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra a aopareceu na posição {}'.format(frase.rfind('A')+1))