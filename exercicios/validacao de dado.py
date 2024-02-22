'''n = int(input('Digite um número de 1 a 50: '))
while n < 1 or n > 50:
    n = int(input('Numero fora do Intervalo, Digite novamente: '))
print('Numero Aceito)

while True:
     n = int(input('Digite um número natural: '))
     if n >= 0: break
print('Número aceito!')

valido = False
while not valido:
    n = int(input('Digite um número inteiro e positivo: '))
'''
n = int(input())
qtd = 0
d = 1

while d <= n:
    if n % d == 0:
        qtd += 1
    d += 1
    
if qtd == 2:
    print('Primo')
else:
    print('Não Primo')
print("Fim")
