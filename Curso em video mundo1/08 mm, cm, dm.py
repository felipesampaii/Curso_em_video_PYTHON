print('======= DESAFIO 08 =======')

medida = float(input('Digite uma distância em metros: '))
mm = medida * 1000
cm = medida * 100
dm = medida * 10
dam = medida / 10
hm = medida / 100
km = medida / 1000
print()
print('A medida de {:.0f}m corresponde à {}mm'.format(medida, mm))
print('A medida de {:.0f}m corresponde à {}cm'.format(medida, cm))
print('A medida de {:.0f}m corresponde à {}dm'.format(medida, dm))
print('A medida de {:.0f}m corresponde à {:.0f}dam'.format(medida, dam))
print('A medida de {:.0f}m corresponde à {:.0f}hm'.format(medida, hm))
print('A medida de {:.0f}m corresponde à {:.0f}km'.format(medida, km))

