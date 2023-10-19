print('{:=^40}'.format(' Matriz em Python '))

matriz = []
for i in range(0, 3):
    linhas = []
    for j in range(0, 3):
        linhas.append(int(input(f'Dígite um valor para posição {i}, {j}: ')))
    matriz.append(linhas)
for i in range (0, 3):
    for j in range (0, 3):
        print(f'[{matriz[i] [j]:^5}]', end='')
    print()
