def ficha(jogador="<desconhecido>", gols=0):
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato')

print('--'*20)
joga = str(input('Nome do Jogador: '))
gol = str(input('Número de Gols: '))
if gol.isnumeric():# verifica se é um numero digitado
    gol = int(gol)
else:
    gol = 0
if joga.strip() == '':# verifica sem mesmo com os espaços removidos tem algum caractere
    ficha(gols=gol)
else:
    ficha(joga, gol)
    