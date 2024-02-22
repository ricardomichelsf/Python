from datetime import date
ano = date.today()
funcionario = {}
funcionario['Nome']= input('Nome: ')
funcionario['Idade'] = ano.year - int(input('Ano de Nascimento: '))
funcionario['cpts'] = int(input('Carteira de trabalho (0 não tem): '))
if funcionario['cpts'] != 0:
    funcionario['contratação'] = int(input('Ano de contratação: '))
    funcionario['salário'] = float(input('Salário: R$ '))
    funcionario['aposentadoria'] = (funcionario['contratação'] + 35) - (ano.year - funcionario['Idade'])
print('-='*25)
print(funcionario)

for chav, val in funcionario.items():
    print(f'{chav} tem o valor {val}')