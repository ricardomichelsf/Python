numeros = [[],[]]
for i in range(1, 8):
    num = int(input(f'Digite o {i}°. valor: '))
    if num % 2 ==0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

print('-='*30)
print(f'Os valores pares digitados foram: {sorted(numeros[0])}')
print(f'Os valores impares digitados foram: {sorted(numeros[1])}')
"""
numeros[0].sort()
numeros[1].sort()
"""