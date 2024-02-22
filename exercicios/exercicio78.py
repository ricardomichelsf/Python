def valor(qual, produt, lista):
    print(f'O {qual} valor digitado foi {produt} na posições ', end='')
    for v, k in enumerate(lista): # percorre a lista e mostra todos as vezes que o numero solicitado apareceu
        if produt == k: 
            print(v, end='... ')
    print()
    
val = []
for va in range(0, 5):
    num = int(input(f'Digite um valor para a posição {va}: '))
    val.append(num)

print(f'Você digitou os valores {val}')
valor('maior', max(val), val)
valor('menor', min(val), val)

