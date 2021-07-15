numero = [5,3,2,1,4,8,9]


indice = 0
while indice < len(numero):
    print(numero[indice], end=" ")
    indice += 1


"""animais = []
resposta = "S"
while resposta == "S":
    resposta = input("DEseja adicionar um animal: ").upper()
    if(resposta == "S"):
        animal = input("Digite o nome do animal: ")
        animais.append(animal) 

print(animais)"""

tupla = tuple(numero)
print(tupla)

print(*tupla)