with open('texte.txt', 'r', encoding='utf-8') as arquivolido:
    linha= arquivolido.readline()
    while linha != '':
        print(linha, end='')
        linha = arquivolido.readline() 

with open('teste2.txt', 'r', encoding='utf-8') as arquivolido1:
    for linha in arquivolido1:
        print(linha, end='')

with open('teste2.txt', 'r', encoding='utf-8') as arquivolido2:
    with open('copiateste.txt', 'w', encoding='utf-8') as arquivocriado1:
        for linha in arquivolido1:
            arquivocriado1.write(linha)
