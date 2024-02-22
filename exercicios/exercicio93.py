jogador = {}
jogador['Nome'] = input('Nome do Jogdor: ')
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogor? '))
jogador['gols']=[]
for i in range(partidas):
    jogador['gols'].append(int(input(f'Quantos gols na partida {i}: ')))
jogador['total'] = sum(jogador['gols'])

print('-='*30)
print(jogador)
print('-='*30)
for chav, val in jogador.items():
    print(f'O campo {chav} tem o valor {val}.')

print('-='*30)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
for par, gol in enumerate(jogador['gols']):
    print(f'{"=>":>6} Na partida {par}, fez {gol} gols.')

print(f'Foi um total de {jogador["total"]} gols.')