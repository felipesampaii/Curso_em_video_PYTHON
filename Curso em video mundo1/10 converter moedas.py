print('======= DESAFIO 10 =======')

real = float(input('Digite a qauntia que deseja comprar: R$ ' ))
dolar = real / 4.88
dolar_canadense = real / 3.89
rublo = real / 0.07
euro =  real / 5.27
libra = real / 6.23
lene = real / 0.03
dolar_australiano = real / 3.56
franco_suico = real / 5.10

print('R$ {:.2f} = US {:.2f}'.format(real, dolar))
print('R$ {:.2f} = C$ {:.2f}'.format(real, dolar_canadense))
print('R$ {:.2f} = ₽ {:.2f}'.format(real, rublo))
print('R$ {:.2f} = € {:.2f}'.format(real, euro))
print('R$ {:.2f} = £ {:.2f}'.format(real, libra))
print('R$ {:.2f} = ¥ {:.2f}'.format(real, lene))
print('R$ {:.2f} = A$ {:.2f}'.format(real, dolar_australiano))
print('R$ {:.2f} = Fr {:.2f}'.format(real, franco_suico))
