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


def moeda(n=0, nota='R$'):
    return f'{nota}{n:>.2f}'.replace('.',',')

