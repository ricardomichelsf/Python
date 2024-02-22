from random import randint
from time import sleep
jogador = {'Jogador1': randint(1, 6), 'Jogador2': randint(1, 6), 'Jogador3': randint(1, 6), 'Jogador4': randint(1, 6)}
print('Valores sorteados:')
for chave, valor in jogador.items():
    sleep(0.5)
    print(f'{"O":>4} {chave} tirou {valor}')

con = 1
print('Ranking dos jogadore:')
for joga in sorted(jogador, key=jogador.get, reverse=True):
    sleep(0.5)
    print(f'{con:>4}° lugar: {joga} com {jogador[joga]}')
    con += 1

"""
from operator import itemgetter
#importa o metodo para ordenar os dados do dicionario pelo numero de pontos e por ordem alfabética
ranking = []
ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)
#o valor 1 no itemgetter vai selecionar o numero sorteado e ordena pela quantidade de vitorias em ordem descrescente
"""