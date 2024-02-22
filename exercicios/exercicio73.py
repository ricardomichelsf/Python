def barra(texto):
    print('=='*30)
    print(texto)
    print('=='*30)
    
times = ('Botafogo', 'Flamengo','Palmeiras', 'Grêmio', 'Fluminense', 
         'Bragantino', 'Athletico Paranaense', 'São Paulo', 'Cuiabá', 
         'Cruzeiro', 'Fortaleza', 'Internacional', 'Atlético Mineiro', 
         'Corinthians', 'Santos',  'Goiás', 'Bahia', 'Coritiba', 'America Mineiro', 'Vasco da Gama')

barra(f'Lista de times do Brasileirão: {times}')
barra(f'Os 5 primeiros são: {times[:5]}')
barra(f'Os 4 ultimos são: {times[-4:]}')
barra(f'Times em ordem alfabética: {sorted(times)}')
if 'Chapecoense' in times:
    barra(times.index('Chapecoense'))
else:
    barra('Chapecoense não está na lista'.center(60))