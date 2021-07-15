nomes_paises =['Brasil', 'Argentina', 'Colombia', 'Japão', 'Canadá']
print(nomes_paises)

print(nomes_paises[1:3])

print(nomes_paises[1:-1])

print(nomes_paises[::2])

print(nomes_paises[::-1])

print("Brasil" in nomes_paises)

print("Canadá" not in nomes_paises)

lista_capitais = []

lista_capitais.append("Brasilila")
lista_capitais.append("Buenos Aires")
lista_capitais.append("Pequim")
lista_capitais.append("Bogota")

print(lista_capitais)

lista_capitais.insert(2, "Paris")
print(lista_capitais)

lista_capitais.remove("Buenos Aires")
print(lista_capitais)

removido = lista_capitais.pop(2)
print(removido)

nome_paises = ("Brasil", "argentina", "China", "canada", 'Japao')
print(nome_paises)

nome_paises = "Brasil", "argentina", "China", "canada", 'Japao'
print(nome_paises, type(nome_paises))

nome_estado = "Sao Paulo",
print(nome_estado, type(nome_estado))

b, a, c, ca, j = nome_paises

print(b, c, j)

print(*nome_paises)
