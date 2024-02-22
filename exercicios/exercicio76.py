lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.00, 
         'Estojo', 25.00, 'Trasnferidor', 4.20, 'Compasso', 9.99, 
         'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('-'*40)
print('LISTAGEM DE PREÇOS'.center(40)) # centraliza o texto
print('-'*40)

for c in range(len(lista)):
    if c % 2 ==0:
        print(f'{lista[c]:.<31}', end='') # deixa o texto alinhado a esquerda e como o marcador(.) no meio
    else:
        print(f'R$ {lista[c]:6.2f}')# deixa o valor formatado

print('-'*40)      