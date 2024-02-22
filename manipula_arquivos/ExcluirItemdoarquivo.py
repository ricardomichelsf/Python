def excluir(lista, palavra):
    new = ''
    for letra in lista:
        if letra != palavra:
            new +=  letra + ' '
    with open('teste_excluir.txt', 'w') as novo:
        novo.write(new)
    

with open('teste_excluir.txt', 'w') as arquivo:
    arquivo.write('Eu consegui fazer a exclusão de um dado em um arquivo')

with open('teste_excluir.txt', 'r+') as arquivo:
    tes = arquivo.readline()
    teste = tes.split(' ')
    ler = 'exclusão'
    excluir(teste, ler)
    