import pandas as pd
from twilio.rest import Client
# Your Account SID from twilio.com/console
account_sid = "AC7XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX69e7e"
# Your Auth Token from twilio.com/console
auth_token  = "your_auth_token"
client = Client(account_sid, auth_token)


# What this application will do.

# Open all the Excel files
# For each file:
# Verify if there's any value in that file is greater than 55.000
#in the Sales colunm
# If the number is greater than 55000 a text message will be
# sent to the Name associated to that sale. In the text will be
# included their Name, the month of the sale and how much he/she
# sold

months_list = ['January', 'February', 'March', 'April', 'May', 'June']

for month in months_list:
    sales_chart = pd.read_excel(f'{month}.xlsx')
    if (sales_chart['Vendas'] > 55000).any():
        sales_person = sales_chart.loc[sales_chart['Sales'] > 55000, 'Salesman'].values[0]
        sales = sales_chart.loc[sales_chart['Sales'] > 55000, 'Sales'].values[0]
        print(f'In the month {month} someone sold more than 55000. That person was {sales_person}, selling {sales}')
        message = client.messages.create(
            to="+15558675309",
            from_="+15017250604",
            body=f'In the month {month} someone sold more than 55000. That person was {sales_person}, selling {sales}')
        print(message.sid)

