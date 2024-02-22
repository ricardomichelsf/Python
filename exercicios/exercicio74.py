from random import randint

valor = (randint(1,10), randint(1,10),randint(1,10), randint(1,10),randint(1,10), randint(1,10))

print('Os valores sorteados foram: ', end=' ')
for n in valor:
    print(n, end=' ')
print()
print(f'O maior valor sorteado foi {max(valor)}')
print(f'O menor valor sorteado foi {min(valor)}')