import requests
import bs4


def check_country():
    ip = input("Введите ip: ")
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}')
        print(response.json()['country'])
    except:
        print("Такого IP не существует")


def check_weather(city):
    response = requests.get(f'https://yandex.ru/pogoda/{city}')
    tree = bs4.BeautifulSoup(response.text, 'html.parser')
    count = 0
    info = []
    for item in tree.select('li', {'class':'link link_theme_normal text forecast-briefly__day-link jSh37Wak link_js_inited'}):
        weather = item.select_one('div', {'class':'forecast-briefly__name'})
        month_date = item.select_one('time', {'class': 'time forecast-briefly__date'})
        if weather != None and month_date != None:
            weather_text = weather.text.split()
            str = ''
            if len(weather_text) > 0:
                i = 0
                res = []
                while not weather.text[i].isdigit():
                    str += weather.text[i]
                    i += 1
                res.append(str)
                str = ''
                while weather.text[i].isdigit():
                    str += weather.text[i]
                    i += 1
                res.append(str)
                info.append(weather.text)
                i += 1
                str = ''
                while weather.text[i] != '+' and weather.text[i] != '−' and weather.text[i] != '0':
                    str += weather.text[i]
                    i += 1
                res.append(str)
        count += 1
    if (len(info) > 8):
        for i in range(1, 9):
            print(info[i])


while True:
    print("1. Определить страну по IP")
    print("2. Узнать погоду")
    n = input("Введите номер задачи: ")
    if n == "1":
        check_country()
    elif n == "2":
        print("Пример ввода: moscow, saint-petersburg, kazan")
        city = input("Введите город: ")
        check_weather(city)
    else:
        print("Неправильно введен номер задачи")
    print()


