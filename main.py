import pandas as pd
from twilio.rest import Client

# Passo a passo da solução (lógica de programação)

# Your Account SID from twilio.com/console
account_sid = ""
# Your Auth Token from twilio.com/console
auth_token = ""
client = Client(account_sid, auth_token)



# Abrir os arquivos em Excel (6)

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho'] # toda lista em python se utiliza []

for mes in lista_meses:                                                   # for = repeat (for variavel in variavel)
# mostra os meses = print(mes)
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
# mostra a tabela completa = print(tabela_vendas)
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês de {mes}, \nos vendedores: {vendedor}, bateram as metas com {vendas} no total de vendas')
        message = client.messages.create(
             to="+",
             from_="+",
             body=f"Parabéns, {vendedor}! você bateu a meta mensal de R$55.000, vendendo um total de {vendas} e ganhou uma viagem para Búzios no fim do ano!")
        print(message.sid)
# Para cada arquivo:

# 1. Verificar se algum valor da coluna 'Vendas' naquele arquivo é maior que R$55.000
# 2. Se for maior que 55.000 -> enviaremos um SMS com o nome, mês e suas vendas.
# 3. Caso não seja maior que 55.000 -> não fazer nada.
