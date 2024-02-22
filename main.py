import pandas as pd
from IPython.display import display
import win32com.client as win32


# Importar a tabela
tabela_vendas = pd.read_excel('Vendas.xlsx')  # lê um arquivo em excel
pd.set_option('display.max_columns', None)  # Mostrar todas as colunas da tabela
display(tabela_vendas)


# Quanto cada loja faturou
print('#'*10)
# coloque sempre entre dois conchetes para indicar as colunas que você quer
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
display(faturamento)

# Quantos produtos cada loja vendeu
qtde_produtos = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
display(qtde_produtos)


print('-'*50)
# Qual foi o ticket medio por produto
ticket_medio = (faturamento['Valor Final'] / qtde_produtos['Quantidade']).to_frame()
ticket_medio = ticket_medio.rename(columns={0: 'Ticket Médio'})
display(ticket_medio)


outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'ricardomsilvaf@gmail.com'
mail.Subject = 'Relatório de Vendas das Lojas'
mail.HTMLBody = f'''
<p> Prezados, </p>

<p> Segue o relatorio de vendas de todas as lojas.</p>

<p>Faturamento:</p>
{faturamento.to_html(formatters={'Valor Total': 'R${:,.2f}'.format})}

<p>Quantidade Vendida:</p>
{qtde_produtos.to_html()}

<p>Ticket Médio dos produtos em cada Loja:</p>
{ticket_medio.to_html(formatters={'Ticket Médio': 'R${:.2f}'.format})}


<p>Qualquer dúvida estou a disposição.</p>

<p>Att..</p>
<p>Ricardo</p>
'''

mail.Send()
print('Email Enviado')
