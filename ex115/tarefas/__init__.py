from ex115.inicio import *


def cadastrar():
    with open('contatos.txt', 'a+') as cadastro:
        nome = cadastro.write(input('Nome:\033[32m '))
        while True:
            val = str(input('\33[mIdade:\033[32m \033[m'))
            if val.isnumeric():
                cadastro.write(val)
                break 
            else:
                print('\033[31mERRO! Digite um número inteiro válido.\033[m')  
            cadastro.write('\n')      
        print(f'Novo registro de {cadastro.read(nome)} adicionado')
        

def mostrar_pessoas():
    with open('contatos.txt', 'rt') as cadastro:
        contat = list(cadastro.readlines())
        for linha in range(len(contat)):
            if linha % 2 == 0:
                print(f'{contat[linha]:<30}', end='')
            else:
                print(f'{contat[linha]:>30}anos')
        print()
            

# Resposta do Guanabara
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('HOuve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1]= dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()
        

def registro(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('HOuve um ERRO na abertura do arquivo:')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados.')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
