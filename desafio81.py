valor = []
while True:
    valor.append(int(input('Digite um valor: ')))
    opc = input('Quer continuar [S/N] / ').strip().upper()
    if opc in'Nn':
        break
print(f'Foram digitados {len(valor)} números')
valor.sort(reverse=True)
print(valor)
if 5 in valor:
    print('Foi digitado o número 5')
else:
    print('O número 5 não foi digitado')

