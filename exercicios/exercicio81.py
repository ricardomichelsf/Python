valores = []
con = True
while con:
    valores.append(int(input('Digite um núemro: ')))
    while True:
        opc = input('Quer continuar [S/N]: ').upper()
        if opc in 'N':
            con = False
            break
        elif opc != 'S':
            print('Não entendi, ', end='')
        else:
            break
print('=-'*30)
valores.sort(reverse=True)
print(f'Você digitou {len(valores)} elementos')
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print(f'O valor 5 faz parte da lista na posição {valores.index(5)}')
else:
    print('O valor 5 não faz parte da lista')