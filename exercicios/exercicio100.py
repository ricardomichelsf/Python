from time import sleep
from random import randint

def sorteia():
    print('Sorteando 5 valores da lista:', end=' ')
    for c in range(5):
        num = randint(1, 10)
        sleep(0.5)
        print(num, end=' ', flush=True)# mostra os numeros sorteados com uma espera, O flush libera para que os numeros aparece de um em um e não todos de uma vez
        numeros.append(num)
    print('PRONTO!')

def somaPar(lis):
    par = 0
    for pa in lis:
        if pa % 2 == 0:
            par += pa
    print(f'Somando os valores pares de {lis}, temos {par}')

numeros = []
sorteia()
somaPar(numeros)