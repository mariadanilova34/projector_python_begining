'''
Взяти API-weather, розпарсити й вивезти погоду від користувача(вводить локацію, по цій локації повернеться погода,
вологість і тд) https://openweathermap.org *Потрібна реєстрація і створення свого api-ключа
'''

import requests

API_key = "02cdc1f9ad297673164afe3839f39ce7"

city_name = input('Enter the City name: ')
city_name_request = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={API_key}")
data_city = (city_name_request.json())

lat, lon = data_city[0]['lat'], data_city[0]['lon']


res_openweather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid='
                               f'{API_key}&units=metric')

match res_openweather.status_code:
    case 200:
        print('\n🟢 All okay, move on\n')
    case 429:
        print('\n🔴 Try later, more request\n')
    case _:
        print(res_openweather.status_code)

data = res_openweather.json()

print(f"☔️ The weather in {data['name']} || {data['sys']['country']}: "
      f"\n🌡 Temperature: {data['main']['temp']}"
      f"\n😮‍💨 Feels like: {data['main']['feels_like']}"
      f"\n👿 Temperature min: {data['main']['temp_min']}"
      f"\n😈 Temperature max: {data['main']['temp_max']}"
      f"\n🤨 Pressure: {data['main']['pressure']}"
      f"\n😅 Humidity: {data['main']['humidity']}"
      f"\n\n☁️ Clouds in {data['name']}: {data['clouds']['all']}%"
      f"\n😶‍🌫️ Visibility in {data['name']}: {data['visibility']}"
      f"\n💨 Wind:"
      f"\n       speed: {data['wind']['speed']}"
      f"\n       deg: {data['wind']['deg']}")