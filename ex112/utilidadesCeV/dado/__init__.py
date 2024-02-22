def verifica(valor):
    val = str(input(valor))
    if val.isnumeric(): # irá verificar se são só numeros
        return float(val)
    # senão for só  numeros ira verificar se tem alguma virgula o se tem letras
    elif val.replace(',','').replace('.','').isnumeric(): # se tiver numeros e virgulas vai tranformar em numerico
        val = float(val.replace(',','.')) 
        return val

def leiaDinheiro(valor):
    val = verifica(valor)
    if type(val) == float: # verifica se o retorno sera um float
        return val
    else:
        while True:
            print('\033[1;31mERRO! Digite um número real válido.\033[m')
            val = verifica(valor)
            if type(val) == float:
                return val
            

# Solução do Guanabara
"""def leiaDinheir(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada =='':
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
        else:
            valido = True
            return float(entrada)
   """
