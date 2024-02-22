extrato = []
deposito = []
saque = []
saldo = numero_saques = 0
limite = 500
limite_saque = 3
print('{:^25}'.format('SISTEMA BANCARIO'))
menu = """Digite a opção desejada:
[1] Deposito
[2] Saque
[3] Extratos
[4] Sair 
Digite: """

while True:
    opc = int(input(menu))
    if opc == 1:
        while True:
            valor = float(input('Valor do deposito R$ '))
            if valor <= 0:
                print('Valor invalido')
            else:
                deposito.append('Deposito')
                deposito.append(valor)
                saldo += valor
                deposito.append(saldo)
                extrato.append(deposito[:])
                deposito.clear()
                break
    elif opc == 2:
        while True:
            valor = float(input('Para sair digite "000", Digite o valor do saque: '))
            if valor <= 500:
                if valor <= saldo and numero_saques < 3:
                    saque.append('Saque')
                    saque.append(valor)
                    print('Saque realizado com sucesso')
                    saldo -= valor
                    saque.append(saldo)
                    numero_saques += 1
                    extrato.append(saque[:])
                    saque.clear()
                else:
                    if valor > saldo:
                        print(f'Saldo insuficiente, Você só tem {saldo:0.2f}')
                        if saldo == 0:
                            valor = 000
                    elif numero_saques == limite_saque:
                        print(f'Limite de saques excedidos {numero_saques}!!')
                        break
            else:
                print("O valor máximo de um saque é de R$ 500, Tente novamente.", end=' ')
            if valor == 000:
                break
    elif opc == 3:
        for val in extrato:
            print(f'{val[0]}: R${val[1]:0.2f}')# pega os valores dentro das sub listas
            print(f'Total: R$ {val[2]:0.2f}')
    elif opc == 4:
        break
    else:
        print('Opção inválida!')

