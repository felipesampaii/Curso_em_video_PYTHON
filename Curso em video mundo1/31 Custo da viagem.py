from time import sleep
distancia = int(input('Qual a distancia da viagem? '))
print(f'A sua viagem é de {distancia}km, iremos calcular o valor... ')
sleep(2)
if distancia <= 200:
    valor1 = distancia * 0.50
    print(f'O valor da passagem é de R${valor1:.2f}')
else:
    valor2 = distancia * 0.45
    print(f'O valor da passagem é de R${valor2:.2f}')

