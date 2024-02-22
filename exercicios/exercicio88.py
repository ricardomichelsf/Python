from random import randint
from time import sleep
apostas = []
numeros = []
print('--'*25)
print('{:^50}'.format('JOGO NA LOTOFACIL'))
print('--'*25)
qtd = int(input('Quantas apostas você deseja: '))
while True:
    num_sorteado = randint(1, 25) # ira sortear os numeros aleatoriamente
    if num_sorteado not in numeros:
        numeros.append(num_sorteado)
    if (len(numeros) == 15 ) and (numeros not in apostas): # verifica se os numeros sorteados ja atingiram a quantidade e se ja existe uma lista igual  
        apostas.append(numeros[:])
        numeros.clear()
    if len(apostas) == qtd:# verifica se ja foram feitas todas as apostas
        break
print('-='*3,  f' SORTEANDO {qtd} JOGOS ', '-='*3)
for quant, jogo in enumerate(apostas):
    sleep(1)
    print(f'Jogo {quant + 1}: {sorted(jogo)}')
print('{:-^50}'.format('  BOA SORTE  '))

