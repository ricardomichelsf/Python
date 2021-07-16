listanum = []
while True:
    num = int(input('Digite um valor: '))
    if num not in listanum:
        listanum.append(num)
    else:
        print('Numero repetido nao irei adicionar')
    opc = input('Deseja adcionar outro número [S/N]: ').strip().upper()[0]
    if opc in 'Nn':
        break
print(sorted(listanum))
