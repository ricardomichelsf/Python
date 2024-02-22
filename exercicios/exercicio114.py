import urllib.request
import requests

try:
    site = requests.get('https://www.youtube.com/') # busca o site na internet
except: # se o site não estiver acessivel irá aparecer essa mensagem de erro
    print('O Site do YouTube não esta acessivel no momento')
else: # se estiver acessivel irá aparecer essa
    print('Consegui acessar o site do YouTube com sucesso')

"""
try:
    site = urllib.request.urlopen('https://www.youtube.com/') 
except:
    print('O Site do YouTube não esta acessivel no momento')
else:
    print('Consegui acessar o site do YouTube com sucesso')
"""

