def fatorial(num, show=False):
    """
    ->Calcule o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (Opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(f' = ', end='')
    return f

print("--" *20)
print(fatorial(5, True))

help(fatorial)