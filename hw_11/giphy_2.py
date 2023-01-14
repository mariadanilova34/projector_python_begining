'''
Create a program that will ask user to search a word. Search this word in Giphy (use their API). Return links to these
GIFs as a result
'''

import requests
import json
from urllib import request, parse
import random

url_ = "http://api.giphy.com/v1/gifs/search"

response = requests.get(url_)

match response.status_code:
    case 200:
        print('\n🟢 All okay, move on\n')
    case 429:
        print('\n🔴 Try later, more request\n')
    case _:
        print(response.status_code)

q = input("Enter your search: ")

params = parse.urlencode({
  "q": q,
  "api_key": "gOfpLk8CDO4WjC05mQoclIhMw5qAYgTO",
  "limit": "5"
})

with request.urlopen("".join((url_, "?", params))) as response:
    data = json.loads(response.read())

gifs = []
num = 0
for names in data['data']:
    gifs.append(names)
    gifs[num] = gifs[num]['url']
    num += 1

print(f"\n✅ Посилання на гіф-анімацію за запитом'{q}': \n{random.choice(gifs)}\n😊 Приємного перегляду 😉")