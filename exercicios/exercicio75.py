valor = (int(input('digite um número: ')), int(input('digite um número: ')), 
         int(input('digite um número: ')), int(input('digite um número: ')))
print(f'Os numeros digitados foram {valor}')
print(f'O número 9 apareceu {valor.count(9)} vezes')
if 3 in valor:
    print(f'O número 3 apareceu na posição {valor.index(3)}')
else:
    print('Não achei o número 3!')
for c in valor:
    if c % 2 ==0 :
        print(c, end=' ')

