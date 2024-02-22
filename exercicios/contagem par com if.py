"""nume = int(input('Digite um inteiro: '))
par = 0
while par <= nume:
    if par % 2 == 0:
        print(par)
    par += 1
print('Fimm')

nume = int(input('Digite um inteiro: '))
par = 0
while par <= nume:
    print(par)
    par += 2
print('Fimm')"""


n = int(input('Digite o n: '))
x = int(input('Digite o x: '))
cont = 1
mult = 0
while mult <= n:
    print(x * cont)
    cont += 1
    mult = x * cont
    
