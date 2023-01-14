# Вивезти всіх космонавтів(кількість і імена) http://api.open-notify.org/astros.json

import requests
import json
from urllib import request

response = requests.get('http://api.open-notify.org/astros.json')

match response.status_code:
    case 200:
        print('\n🟢 All okay, move on\n')
    case 429:
        print('\n🔴 Try later, more request\n')
    case _:
        print(response.status_code)

with request.urlopen('http://api.open-notify.org/astros.json') as response:
    data = json.loads(response.read())

astronauts = []
num = 0
for names in data['people']:
    astronauts.append(names)
    astronauts[num] = astronauts[num]['name']
    num += 1

print(f"👩🏻‍🚀🚀 Кількість космонавтів в космосі: {data['number']}\n💫 Імена космонавтів в космосі: {astronauts}")