from lib.interface import * # como o arquivo sistema esta dentro do msm pacote não precisa colocar o nome do pacote
from lib.arquivo import *
from time import sleep


arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Mostrar Pessoas Cadastradas', 'Cadastrar Pessoas', 'Sair'])
    if resposta == 1:
        lerArquivo(arq)
        print(linha())
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastro(arq, nome, idade)
        print(linha())
    elif resposta == 3:
        cabecalho('Saindo do Sistema... Até logo')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida.\033[m')
    sleep(1)

