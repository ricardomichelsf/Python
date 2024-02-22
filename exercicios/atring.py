"""curso = ' Curso de Python'
print(len(curso.strip()))"""

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Bacon')
"""print('Eu vou comer ',end='')
for n, c in enumerate(lanche):
    if n < len(lanche) - 1:
        print(c,end=', ')
    else:
        print(c)"""

for cont in range(len(lanche)):
    if cont < len(lanche) - 1: # verifica se é o ultimo item da lista
        print(lanche[cont],end=', ')
    else:
        print(lanche[cont])
