pessoas = []
nome = []
nota = []
while True:
    nome.append(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    nota.append(nota1)
    nota.append(nota2)
    nome.append(nota[:])
    pessoas.append(nome[:])
    nota.clear()
    nome.clear()
    opc = input('Quer continuar? [S/N]: ').upper()
    if opc in 'N':
        break

print('-='*25)
print('{:<1}  {:^7} {:>10}'.format('No.', 'NOME', 'MÉDIA'))
print('-'*30)
for pos, linha in enumerate(pessoas):
    print('{:<1}'.format(pos),end=' ')
    for colun , pes in enumerate(linha):
        if colun == 0:
            print('{:^13}'.format(pes), end=' ')
        else:
            media = div = 0
            for resu in pes: # pecorre a lista das notas 
                media += resu
                div += 1 # adiciona quantas elementos tem na lista
                media /= div
            print('{:>6}'.format(round(media, 1)))# deixa o numero float com só 1 casa decimal

while True:
    print('--'*25)
    most = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if most == 999:
        print('FINALIZANDO...')
        print('<<< VOLTE SEMPRE >>>')
        break
    else:
        print(f'Notas de {pessoas[most][0]} são {pessoas[most][1]}')

"""
ficha = []
while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/ 2
    ficha.append([nome, [nota1, nota2], media])
    resp = input('Quer continuar? [S/N]: ')
    if resp in 'Nn':
        break

print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'* 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')

"""
