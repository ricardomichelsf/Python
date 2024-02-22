def aumentar(n, aumen, format=False):
    n = n + (n * (aumen/100))
    return n if format is False else moeda(n)# verifica se o valor do format se True ele ira mostrar a formatação


def diminuir(n, dimi, format):
    n = n - (n * dimi/100)
    return n if not format else moeda(n)# verifica se o valor do format se True ele ira mostrar a formatação


def dobro(n, format):
    n = n * 2
    if format == True:
        n = moeda(n)
    return n


def metade(n, format):
    n = n / 2
    if format == True:
        n = moeda(n)
    return n


def moeda(n):
    return f'R$ {n:.2f}'.replace('.',',')

