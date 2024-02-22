from lib.interface import *
def arquivoExiste(nome):
    try:
        with open(nome, 'r') as a: # x cria um arquivo caso não tenha 
            pass
    except FileNotFoundError:
        return False
    else:
        return True
    

def criarArquivo(nome):
    try:
        with open(nome, 'wt+') as a:
            pass
    except:
        print('Houve um ERRO na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'r')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','') # troca o quebrador de linha por um espaço para ficar organizado qndo mostrar
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastro(arquivo, nome = 'desconhecido', idade = 0):
    try:
        arq = open(arquivo, 'a')
    except:
        print('Houve um ERRO na abertura do arquivo')
    else:
        try:
            arq.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de gravar os dados')
        else:
            print(f'Novo registro {nome} adicionado com sucesso!')
            arq.close()



