# Haoyan Ou Assignment 2C

f1 = 1.09
f2 = 7.82
f3 = 7.12
# f1 is the exchange rate between EUR and USD.
# f2 is the exchange rate between RMB and EUR.
# f3 is the exchange rate between RMB and USD

print('Welcome to the 3-currency calculator!')
amount = int(input('Please enter the From amount: '))
from_currency = input('Please enter the From currency (USD, EUR or RMB): ')
to_currency = input('Please enter the To currency (USD, EUR or RMB): ')

if from_currency == 'EUR':
    if to_currency == 'USD':
        USD_currency = amount*f1
        print(f'{amount} EUR equals to {USD_currency} USD.')
    elif to_currency == 'RMB':
        RMB_currency = amount*f2
        print(f'{amount} EUR equals to {RMB_currency} RMB.')
    else:
        print('Error.')
elif from_currency == 'USD':
    if to_currency == 'EUR':
        EUR_currency = amount/f1
        print(f'{amount} USD equals to {EUR_currency: .2f} EUR.')
    elif to_currency == 'RMB':
        RMB_currency = amount*f3
        print(f'{amount} USD equals to {RMB_currency} RMB.')
    else:
        print('Error.')
elif from_currency == 'RMB':
    if to_currency == 'EUR':
        EUR_currency = amount/f2
        print(f'{amount} RMB equals to {EUR_currency: .2f} EUR.')
    elif to_currency == 'USD':
        USD_currency = amount/f3
        print(f'{amount} RMB equals to {USD_currency: .2f} USD.')
    else:
        print('Error.')
else:
    print('Error.')