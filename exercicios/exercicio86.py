matriz = [[],[],[]]
for linha in range(3):
    for coluna in range(3):
        matriz[linha].append(int(input(f'Digite um valor para [{linha}, {coluna}]: ')))

print('-='*30)
for linha in matriz:
    for coluna in linha:
        print(f'[ {coluna:^5} ]', end=' ')
    print()