pessoas = []
dados = []

while True:
    dados.append(input('Nome: '))
    dados.append(int(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    opc = input('Quer continuar? [S/N] ').upper()
    if opc == 'N':
        break
maior = 0
for mas in pessoas:
    if mas[1] > maior:
        maior = mas[1]
print('-='*35)
print(f'Ao todo você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi {float(maior)} Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(p[0], end=', ')
menor = maior
for mas in pessoas:
    if mas[1] < menor:
        menor = mas[1]
print(f'\nO menor peso foi {float(menor)} Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(p[0], end=', ')


"""
while True:
    dados.append(input('Nome: '))
    dados.append(int(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1]>maior:
            maior=dados[1]
        if dados[1] < menor:
            menor=dados[1]
    pessoas.append(dados[:])
    dados.clear()
    opc = input('Quer continuar? [S/N] ').upper()
    if opc == 'N':
        break
"""
