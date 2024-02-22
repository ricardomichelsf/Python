from time import sleep

def maior(*args):
    print('-='*25)
    print('Analisando os valores passados ...')
    maior = 0
    if args != 0:
        for c in args:
            print(c, end=' ', flush=True)
            sleep(0.6)
            if c > maior:
                maior = c
    print(f'Foram informados {len(args)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')

seis = maior(2, 9, 4, 5, 7, 1)
tres = maior(4, 7, 0)
dois = maior(1, 2)
um = maior(6)
num = maior()