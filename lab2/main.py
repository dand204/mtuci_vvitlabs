from time import sleep
import requests

APP_KEY = "!!! API KEY !!!"

CITIES = {
    1: "Moscow,RU",
    2: "Saint Petersburg,RU",
    3: "Kazan,RU",
    4: "Samara,RU",
    5: "Yekaterinburg,RU",
    6: "Novosibirsk,RU",
    7: "Khabarovsk,RU",
    8: "Vladivostok,RU"

}


# <-------------------------------------------------------------------------------------------------------------->
def session():
    global CITIES
    try:
        CITY_NAME = CITIES.get(choose_city())

        data_current = request_data(str(CITY_NAME), APP_KEY, 'weather')
        show_result_current(data_current, CITY_NAME)

        data_forecast = request_data(str(CITY_NAME), APP_KEY, 'forecast')
        show_result_forecast(data_forecast, CITY_NAME)

    except ValueError:
        print("Неверно указан номер города.")
        sleep(2)
        session()
    except KeyError:
        print("Не удалось получить данные о погоде")


def choose_city():
    print(
        "Доступные города: \n 1) Москва \n 2) Санкт-Петербург \n 3) Казань \n 4) Самара \n 5) Екатиринбург \n 6) "
        "Новосибирск \n 7) Хабаровск \n 8) Владивосток")

    CITY = int(input("Укажите номер города: "))
    if 0 < CITY <= len(CITIES):
        return CITY
    else:
        raise ValueError


def request_data(CITY_NAME, APPID, REQ_TYPE):
    res = requests.get(("http://api.openweathermap.org/data/2.5/" + REQ_TYPE),
                       params={'q': CITY_NAME, 'units': 'metric', 'lang': 'ru', 'APPID': APPID})
    data = res.json()
    return data


def show_result_current(data, s_city):
    print("Город:", s_city)
    print("Погодные условия:", data['weather'][0]['description'])
    print("Температура:", data['main']['temp'])
    print("Минимальная температура:", data['main']['temp_min'])
    print("Максимальная температура", data['main']['temp_max'])


def show_result_forecast(data, s_city):
    print('Нажмите ENTER чтобы вывести недельный прогноз')
    if input() != 0:
        print("Прогноз погоды на неделю в городе " + s_city + " :")
        for i in data['list']:
            print("Дата <", i['dt_txt'], "> \r\nТемпература <",
                  '{0:+3.0f}'.format(i['main']['temp']), "> \r\nПогодные условия <",
                  i['weather'][0]['description'], "> \r\nСкорость ветра <",
                  i['wind']['speed'], "> \r\nВидимость <",
                  i['visibility'], ">")
            print("____________________________")


session()
