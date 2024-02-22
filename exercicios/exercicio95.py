joga = []
jogador = {}
while True:
    jogador.clear() # limpa o dicionario original só deixa a copia dentro da lista
    print('--'*20)
    jogador['nome'] = input('Nome do Jogador: ')
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogor? '))
    jogador['gols']=[]
    for i in range(partidas):
        jogador['gols'].append(int(input(f'Quantos gols na partida {i}: ')))
    jogador['total'] = sum(jogador['gols'])
    joga.append(jogador.copy())# copia o dicionario para a lista
    opc = input('Quer continuar? [S/N] ').upper()
    if opc == 'N':
        break

print('-='*30)
print("cod ", end='')
for i in jogador.keys():# esse loop irá pegar as chaves do dicionario e print ja foramtada
    print(f'{i:<15}', end='')
print()
print('--'*25)
for indi, conteud in enumerate(joga):
    print(f'{indi:>3} ', end='')
    for val in conteud.values():# esse loop irá pegar os valores do dicionario e print ja formatada
        print(f'{str(val):<15}', end='')
    print()

print('-='*30)
print(joga)
while True:
    mostr = int(input('Mostrar dados de qual jogador? '))
    if mostr == 999:
        break
    elif mostr >= len(joga):
        print(f'ERRO! Não existe jogador com o código {mostr}!. Tente novamente')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {joga[mostr]["nome"]}:')
        for par, gol in enumerate(joga[mostr]['gols']):
            print(f'{" ":>5} No jogo {par}, fez {gol} gols.')
    

