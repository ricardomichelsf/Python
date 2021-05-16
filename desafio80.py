lista = []
for c in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
    if lista == (max(lista)):
        lista.insert(5)
        print('Adicionado na ultimma posição')
print(f'Os valores digitados foram {lista}')
