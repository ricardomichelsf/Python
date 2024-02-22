numeros = []
pares = []
impar = []
while True:
    valor = int(input('Digite um núemro, se quiser sair digite 000: '))
    if valor == 000:
        break
    numeros.append(valor)
    if valor % 2 ==0:
        pares.append(valor)
    else:
        impar.append(valor)

print(f'Os valores digitados foram {numeros}')
print(f'Esses são os valores pares digitados {pares}')
print(f'Esses são os valores impares digitados {impar}')
print('-=-'*30)