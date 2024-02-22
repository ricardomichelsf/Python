matriz = [[],[], []]
for linha in range(3):
    for coluna in range(3):
        matriz[linha].append(int(input(f'Digite um número para [{linha}, {coluna}]: ')))

par = soma = 0
print('-='*35)
for linha in matriz:# pega cada linha da matriz e percorre
    for coluna in linha:# pega cada linha e cria as colunas
        print(f'[ {coluna:^5} ]', end=' ')
        if coluna % 2 ==0:
            par += coluna
        if linha.index(coluna) == 2:
            soma += coluna
    print()

print('-='*35)
print(f'A soma dos valores pares é {par}')
print(f'A soma dos valores da terceira coluna é {soma}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
