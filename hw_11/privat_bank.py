import requests
from math import *

res_privatbank = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5')

match res_privatbank.status_code:
    case 200:
        print('\n🟢 All okay, move on\n')
    case 429:
        print('\n🔴 Try later, more request\n')
    case _:
        print(res_privatbank.status_code)


your_money = input("💸 Enter your sum to change in UAH: ")

my_currencies = {
    'USD': '🇺🇸',
    'EUR': "🇪🇺"
}

my_rates = []
for obj in res_privatbank.json():
    if obj['ccy'] in my_currencies and obj not in my_rates:
        my_rates.append(obj)


for obj in my_rates:
    print(f"\nВалюта: {my_currencies[obj['ccy']]} \nКупівля {round(int(your_money)*float(obj['buy']), 2)} "
          f"\nПродаж: {round(int(your_money) * float(obj['sale']),2)}")