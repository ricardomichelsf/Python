from Funcoes.funcoes_arquivos import *
inventario = {}
opc = chamarMenu()

while opc > 0 and opc < 4:
    if opc == 1:
        registrar(inventario)
    elif opc == 2:
        persistir(inventario)
    elif opc == 3:
        print(exibir())
    opc = chamarMenu()
