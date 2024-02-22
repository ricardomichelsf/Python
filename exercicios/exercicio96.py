def area(largu, compri):
    are = largu * compri
    print(f'A área de um terreno {largu} x {compri} é de {are}m².')


print(' Controle de Terrenos')
print('-'*24)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)
