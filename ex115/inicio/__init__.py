from ex115.tarefas import *

'''tamanho = 45

def formata(msg):
    global tamanho
    print('-'*tamanho)
    print(msg.center(tamanho))
    print('-'*tamanho)

def main():
    while True:
        formata('MENU PRINCIPAL')
        print("""1 - Mostrar pessoas cadastrados
2 - Cadastrar novo pessoa
3 - Sair do Sistema """)
        print('-'*tamanho)
        escolha = int(input("\033[33mSua Opção:\033[32m \033[m\033[m"))

        if escolha < 1 or escolha >3:
            print('\033[31m ERRO! digite uma opçãp válida!. \033[m')
            continue
        elif escolha == 1:
            formata('PESSOAS CADASTRADAS')
            mostrar_pessoas()
        elif escolha == 2:
            formata('NOVO CADASTRO')
            cadastrar()
        elif escolha == 3:
            formata('Saindo do sistema...  Até logo!')
            break'''


# Resposta do Guanabara

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31m Usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def linha(tam = 42):
    return '-'* tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32msua opção: \033[m')
    return opc

