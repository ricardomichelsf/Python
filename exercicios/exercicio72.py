numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
             'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 
             'dezeoito', 'dezenove', 'vinte')

cont = True
while cont:
    num = int(input('Digite um número entre 0 e 20: '))
    if num in range(len(numeros)):
        print(f'Você digitou o número {numeros[num]}')
        while True:
            opc = input('Quer continuar [S/N]: ').upper()
            if opc in 'N':
                cont = False
                break
            elif opc != 'S':
                print('Não entendi! ', end='')
            else:
                break
    else:
        print('Tente novamente. ', end= '')
   
