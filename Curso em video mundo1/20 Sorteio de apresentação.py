print('======= DESAFIO 20 =======')
import random

n1 = str(input('Grupo 1: '))
n2 = str(input('Grupo 2: '))
n3 = str(input('Grupo 3: '))
n4 = str(input('Grupo 4: '))
lista = [n1, n2, n3, n4]
sorteio = random.shuffle(lista)
print('A ordem dos grupos para a apresentação do trabalho é')
print(f'{lista}')