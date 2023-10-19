print('======= DESAFIO 19 =======')

import random

b = str('Bitcoin')
e = str('Ethereum')
s = str('Shiba inu')
ba = str('Baby doge')
a = str('Cardano')
sl = str('Solana')

lista = [b, e, s, ba, a, sl]
escolhido = random.choice(lista)

print(f'{escolhido}')