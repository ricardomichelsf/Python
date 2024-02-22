pare = []
expre = input('Digite uma expressão: ')
for ex in expre:
    if '(' == ex:
        pare.append(ex)
    elif ')' == ex and '(' in pare: # irá verifcar se ')' é igual a o valor do for e '(' está na expressão se tiver ira apaga-lo
        pare.remove('(')
    elif ')' == ex and '(' not in pare: #senão encontra o '(' será adicionado a lista o ')'
        pare.append(ex)

if pare == []:
    print('Sua expressão é válida')
else:
    print('Sua expressão é inválida')
