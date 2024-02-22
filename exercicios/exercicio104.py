def leiaInt(num):
    nu = str(input(num))
    if nu.isnumeric():
        return nu
    else:
        while True:
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
            nu = input(num)
            if nu.isnumeric():
                return nu

n = leiaInt('Digite um número inteiro: ')
print(f'Você digitou o número {n}')