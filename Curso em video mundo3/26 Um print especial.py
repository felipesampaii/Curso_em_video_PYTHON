print('{:=^40}'.format(' Um print especial '))

def escreva(msg):
    tam = len(msg) + 4
    print('-' * tam)
    print(f' {msg}')
    print('-' * tam)

escreva('felipe Galdino de Sampaio')
escreva('Estou cursando Python com o professor guanabara')
