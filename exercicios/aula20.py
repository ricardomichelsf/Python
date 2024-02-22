"""def dobra(lst):
    pos = 0
    while pos < len(lst): # pecorre a lista
        lst[pos] *= 2 # verifica o numero da lista na posição indicada o dobra o valor 
        pos +=1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)"""

def soma(* valores):# o * vai receber todos os valores independente da quantidade informada
    s = 0
    print('Somando os valores:', end=' ')
    for pos, num in enumerate(valores):
        s += num
        if pos != len(valores) - 1:# verifica se não é o ultimo numero 
            print(num, end= ', ')
        else:# se for o ultimo numero ele não colocara a virgula depois do número
            print(num, end=' ')
    print(f'temos {s}')


soma(5, 7)
soma(2, 9, 4)
soma(8, 4, 6, 5, 3, 1, 7)