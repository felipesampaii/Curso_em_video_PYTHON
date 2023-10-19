radar = int(input('Qual a velocidade atual do carro? '))
if radar <= 80:
    print('Tenha um bom dia! e dirija com segurança!')
else:
    multa = (radar -80)* 7
    print('MULTADO! Você excedeu o limite  permitido que é 80km/h'
          f'você deve pagar uma multa de R${multa:.2f}')
