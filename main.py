import pandas as pd    # pd é abreviação para utilizar o pandas dentro do programa
from twilio.rest import Client

#pandas - integração do python com o excel
#openpyxl - integração do python com o excel
#twilio - integração do python com o sms
account_sid = "ACcea710f515e96dc4cb1aa23999537fb2"
auth_token = "9bee2af0430110798a43deb8e47feabd"
client = Client(account_sid, auth_token)

#Solução

#Abri 6 arqivos em excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    #print(mes)

    #pede para uma variavel receber o mes expecifico
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')

    #print(tabela_vendas)

    #se algum valor dentro da coluna vendas for maior que 55000
    if (tabela_vendas['Vendas'] > 55000).any():
        #.loc é para localizar na tabela   / .values[0] para pegar o valor
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mes de {mes} alguém bateu a meta. Vendedor {vendedor}, Vendas: {vendas}')
        # Se for maior que 55.000 -> envia um SMS com nome, o mes e as vendas dele
        message = client.messages.create(
            to="+5522999655402",
            from_="+18608095718",
            body=f'No mes de {mes} alguém bateu a meta. Vendedor {vendedor}, Vendas: {vendas}')
        print(message.sid)


