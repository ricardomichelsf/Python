from time import sleep
c = ['\033[m',        # 0 - sem cor
     '\033[0;30;41m',  # 1 vermelho
     '\033[0;30;42m',  # 2 - verde
     '\033[0;30;43m',  # 3 - amarelo
     '\033[0;30;44m',  # 4 - azul
     '\033[0;30;45m',  # 5 - roxo
     '\033[7;30m']    # 6 - branco


def ajuda(com):
    formata(f'Acessando o manual do comando \' {com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def formata(msg, cor=0):
    conta = len(msg) + 4
    print(c[cor], end='')
    print('~'*conta)
    print(f'  {msg}')
    print('~'*conta)
    print(c[0], end='')
    sleep(1)


comando = ''
while True:
    formata('SISTEMA DE AJUDA PYHELP', 2)
    comando = str(input('Função ou Biblioteca > ')).lower()
    if comando == 'fim':
        break
    else:
        ajuda(comando)
formata('ATÈ LOGO !', 1)


""" frase = 'SISTEMA DE AJUDA PYHELP'
formata(frase, 2)
while True:
    ajuda = str(input('Função ou Biblioteca: ')).lower()
    if ajuda == 'fim':
        frase = 'ATÉ LOGO !'
        formata(frase, 5)
        break
    texto = 'Acessando o manual do comando ' + ajuda
    formata(texto, 4)
    help(ajuda) 
"""
