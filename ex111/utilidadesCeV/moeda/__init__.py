def aumentar(n, aumen):
    n = n + (n * (aumen/100))
    n = moeda(n)
    return n


def diminuir(n, dimi):
    n = n - (n * dimi/100)
    n =moeda(n)
    return n


def dobro(n):
    n = n * 2
    n = moeda(n)
    return n


def metade(n):
    n = n / 2
    n = moeda(n)
    return n


def moeda(n):
    return f'R$ {n:>.2f}'.replace('.',',')

def resumo(valor, aumen, descon):
    """
    -> Valor: receber o valor apresentado
    -> Aume: recebe o percentual de aumento
    -> Porce: recebe a porcentagem de desconto
    """
    print('-'*35)
    print(f'{"RESUMO DO VALOR":^35}')
    print('-'*35)
    print(f'Preço analisado: \t{moeda(valor)}') # o \t cria um espaço separando as strings
    print(f'Dobro do preço: \t{dobro(valor)}')
    print(f'Metade do preço: \t{metade(valor)}')
    print(f'{aumen}% de aumento: \t{aumentar(valor, aumen)}')
    print(f'{descon}% de redução: \t{diminuir(valor, descon)}')
    print('-'*35)