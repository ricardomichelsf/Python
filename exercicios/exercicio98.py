from time import sleep
def contador(ini, fim, passo):
    print('-='*20)
    if passo == 0:
        passo = 1
    elif passo < 0:
        passo = -(passo)
    print(f'Contagem de {ini} até {fim} de {passo} em {passo}')
    if fim < ini:
        while ini >= fim:
            print(ini, end=' ', flush=True)# o flush ele força o sistema a mostrar o resultado sem precisar esperar o proximo
            sleep(0.5)
            ini -=passo
    elif fim > ini:
        while ini <= fim:
            print(ini, end=' ', flush=True)
            sleep(0.5)
            ini += passo
    print('FIM!')


cont = contador(1, 10, 1)
conta = contador(10, 0, 2)
print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
inic = int(input('Início: '))
final = int(input('Fim: '))
pas = int(input('Passo: '))
contador(inic, final, pas)
