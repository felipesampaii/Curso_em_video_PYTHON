print('======= DESAFIO 15 =======')

dia = int(input('Por quantos dias o carro foi alugado?: '))
km = float(input('Quantos km o carro andou?: '))

ckm = km * 0.15
cdia = dia * 60
t = ckm + cdia
print(f'O valor total a pagar é de R${t:.2f}')