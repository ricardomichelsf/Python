ano = input().split(" ")

for i in ano:
    ano1 = int(ano)
    if i < 1000:
        print('Ano Invalido')
    elif ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
            print('O ano {} é BISSEXTO'.format(ano))
    else:
            print('O ano {} não é BISSEXTO'.format(ano))

