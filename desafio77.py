palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for b in palavras:
    print(f'\nNa palavra {b.upper()} temos ', end='')
    for letra in b:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')