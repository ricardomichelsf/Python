from ex115.inicio import *
from ex115.tarefas import *

#inic = main()


# Resposta do Guanabara

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu('Ver Pessoas Cadastradas', 'Cadastrar Pessoas', 'Sair do Programa')
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        registro(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até Logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida\033[m')
