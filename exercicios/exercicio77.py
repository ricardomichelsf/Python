palavras = ('armario', 'palanque', 'relogio', 'pyhton', 'ciencia', 'cama', 'transar', 'dinheiro')

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos ', end='')
    for pala in palavra:
        if pala in 'aeiou': # verifica as vogais dentro da palavra
            print(pala,end=' ')
