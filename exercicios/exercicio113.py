from ex112.utilidadesCeV import dado

def leiaInt(numero):
    valor = str(input(numero)).strip()# o strip ignora os espaços em branco
    if valor.isnumeric():
        return valor
    else:
        while True:
            print('\033[01;31mERRO! Digite um número Inteiro valido. \033[m ')
            valor = input(numero)
            if valor.isnumeric():
                return valor
            

try:
    inteiro = leiaInt('Digite um número inteiro: ')
except KeyboardInterrupt:# verifica se o usuário interrompeu o programa CRTL + C
    print('\033[31m \nO usuário prefiriu não digitar nenhum número\033[m')
    inteiro = 0
else:
    inteiro


try:
    real = dado.leiaDinheiro('Digite um número real: ')
except KeyboardInterrupt:# verifica se o usuário interrompeu o programa CRTL + C
    print('\033[31m \nO usuário prefiriu não digitar nenhum número\033[m')
    real = 0
else:
    real
print(f'Você digitou o número Inteiro {inteiro} e o real foi {real}')


# solução do guanabara
"""
def leiaInt(numero):
    while True:
    try:
        n = int(input(numero))
    except (ValueError, TypeError):
        print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
        continue
    except KeyboardInterrupt:
        print('\n\033[31mUsuário preferiu não digitar esse número.\033[m)
    else:
        return n
"""