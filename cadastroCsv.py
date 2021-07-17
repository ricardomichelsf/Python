import csv
header = ['nome', 'sobrenome']
dados = []
option = input('O que deseja fazer?\n1 - Cadastrar\n0 - Sair\n')
while option != '0':
    nome = input("Qual o seu nome? ")
    sobrenome = input("Qual o seu sobrenome? ")
    dados.append([nome, sobrenome])
    option = input('O que deseja fazer?\n1 - Cadastrar\n0 - Sair\n')

print(dados)

with open('users.csv', 'w', newline='') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    writer.writerow(header)
    writer.writerow(dados)

with open('users.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)
