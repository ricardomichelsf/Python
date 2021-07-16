import csv

with open("brasil_covid.csv", 'r', encoding='utf-8') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    heard = next(leitor)
    for linha in leitor:
        if float(linha[2]) > 1:
            print(linha)

