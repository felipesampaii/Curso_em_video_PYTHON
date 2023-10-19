print('{:=^40}'.format(' Maior e Menor valores '))

resp = 'S'
soma = quant = média = 0
while resp in 'Ss':
    n1 = int(input('Dígite um número: '))
    soma += n1
    quant += 1
    if quant == 1:
        maior = menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor < n1
    resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
média = soma / quant

print(f'Você dígitou {quant} números, a soma entre todos eles é de {soma} e a média geral é de {média:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
