from Funcoes.funcoes_dicionario import *

usuarios = {}
main = inicio()

while True:
    if main == 'I':
        inserir(usuarios)
    elif main == 'P':
        pesquisar(usuarios, input("Quem você deseja procurar? "))
    elif main == 'L':
        listar(usuarios)
    elif main == 'E':
        excluir(usuarios, input('Quem você deseja excluir? '))
    elif main == 'S':
        print('Programa finalizado, Volte Sempre!!!..')
        break
    main = inicio()