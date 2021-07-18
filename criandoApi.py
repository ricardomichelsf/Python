import requests

url = 'https://api.exchangerate-api.com/v6/latest'

request = requests.get(url)

print(request.status_code)

dados = request.json()

valor_reais = float(input("Informe o valor em  R$ a ser convertido\n"))
cotacao = dados['rates']['BRL']
print(f'R${valor_reais} em dólar valem U$ {(valor_reais / cotacao):.2f}')