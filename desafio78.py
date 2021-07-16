valores = []
mai = men = 0
for v in range(0,5):
    valores.append(int(input(f'Digite um valor para a posicão {v}: ')))
print('=='*30)
print(f'Você digitou os números {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posição ', end='')
for i, v in enumerate(valores):
    if v == max(valores):
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {min(valores)} nas posiçôes ', end='')
for i, v in enumerate(valores):
    if v == min(valores):
        print(f'{i}... ', end='')
