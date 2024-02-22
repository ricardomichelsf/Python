aluno ={}
aluno['Nome'] = input('Nome: ')
aluno['Média'] = float(input(f'Media de {aluno["Nome"]}: '))
print(f'Nome é igual a {aluno["Nome"]}')
print(f'Média é igual a {aluno["Média"]}')
if aluno['Média'] >= 7:
    print('Situação é igual a Aprovado')
else:
    print('Situação é igual a Reprovado')