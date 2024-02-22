lista = []
while True:
    num = int(input('Digite um numéro, caso queira parar digite 000: '))
    if num == 000:
        break
    elif num not in lista:
        lista.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado não vou adicionar...')
        
lista.sort()
print(lista)