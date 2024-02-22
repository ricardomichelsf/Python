pessoas = []
ficha = {}
soma = media =0
while True:
    ficha['nome'] = input('Nome: ')
    ficha['sexo'] = input('Sexo: [M/F] ').upper()
    ficha['idade'] = int(input('Idade: '))
    soma += ficha['idade']
    pessoas.append(ficha.copy())
    ficha.clear()
    opc = input('Quer continuar? [S/N] ').upper()
    if opc == 'N':
        break

print('-='*30)
print(f'- O grupo tem {len(pessoas)} pessoas')
media = soma/len(pessoas)
print(f'- A média de idade é de {media:5.2f} anos')
print('- As mulheres cadastradas foram: ',end='')
for iten in pessoas:
    for ke, val in iten.items():
        if ke == 'sexo' and val == 'F':
            print(iten['nome'], end=' ')
"""
for iten in pessoas:
    if iten['sexo']=='Ff':
        print (iten ['nome'], end=' ')
"""
print('\n- Lista das pessoas que estão acima da média:')
for iten in pessoas:
    for k, v in iten.items():
        if k == 'idade' and float(v) > float(media):
            print()
            print(f'Nome = {iten["nome"]}; Sexo = {iten["sexo"]}; Idade = {iten["idade"]}')
           # print(f'{iten[k]} = {iten[v]}', end=': ')
"""
for iten in pessoas:
    if iten['idade'] >= media:
        print(' ')
        for k, v in iten.items()
            print(f'{k} = {v} ', end=' ')
        print()
"""
print('<< ENCERRADO >>')