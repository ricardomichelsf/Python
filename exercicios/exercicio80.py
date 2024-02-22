valor = []
for v in range(0, 5):
    num = int(input('Digite um valor: '))
    valor.append(num)
    for val in valor: # percorre a lista
        if num < val: # verifica se o valor digitado é menor que o valor encontrado na lista 
            valor.remove(num)
            valor.insert(valor.index(val), num) # coloca o valor menor no posição do outro
            break
    print(f'O número foi adicionado na posição {valor.index(num)}')

print(valor)
