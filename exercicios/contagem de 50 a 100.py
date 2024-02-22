intervalo_50 = 50
while intervalo_50 <= 100:
    print(intervalo_50, end='-')
    intervalo_50 += 1
print('fim')


from time import sleep
print('VAMOS LANÇAR UM FOGUETE')
contagem = 10
while contagem >= 1:
    print(contagem)
    sleep(0.1)
    contagem -= 1
print('FOGO')
