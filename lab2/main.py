import requests
import telebot
import datetime
from dotenv import load_dotenv
import os

load_dotenv("./.env")
owm_key = os.getenv('OPENWEATHERMAP_API_KEY')
telegram_key = os.getenv('TELEGRAM_API_KEY')

try:
    bot = telebot.TeleBot(telegram_key)
except:
    print("Telegram bot is not started! ")
    exit()

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


@bot.message_handler(commands=['start'])
def command_start(msg):
    keyboard = telebot.types.ReplyKeyboardMarkup()
    keyboard.row('Текущий прогноз', 'Недельный прогноз')
    bot.send_message(msg.chat.id, 'Привет! С помощью данного бота можно узнать актуальный прогноз погоды.',
                     reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def response_with_text(msg):
    if msg.text == 'Текущий прогноз':
        call_request(msg, 'weather')
    if msg.text == 'Недельный прогноз':
        call_request(msg, 'forecast')


# <-------------------------------------------------------------------------------------------------------------->


def call_request(msg, call_type):
    bot.send_message(msg.chat.id, 'Укажите город для которого хотите посмотреть погоду',
                     reply_markup=gen_city_choice())
    try:
        def received(callbackid):
            chosen_city = callbackid
            CITY_NAME = CITIES.get(chosen_city)
            data_current = request_data(str(CITY_NAME), owm_key, call_type)
            if call_type == 'weather':
                show_result_current(data_current, CITY_NAME, msg)
            if call_type == 'forecast':
                show_result_forecast(data_current, CITY_NAME, msg)

        call_request.recieved = received
    except KeyError:
        bot.send_message(msg.chat.id, 'Произошла ошибка!')


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    return call_request.recieved(int(call.data))


def request_data(CITY_NAME, APPID, REQ_TYPE):
    res = requests.get(("http://api.openweathermap.org/data/2.5/" + REQ_TYPE),
                       params={'q': CITY_NAME, 'units': 'metric', 'lang': 'ru', 'APPID': APPID})
    data = res.json()
    return data


def show_result_current(data, s_city, msg):
    content = ("Город:" + ' ' + str(s_city)) + '\n' + (
            "Погодные условия:" + ' ' + str(data['weather'][0]['description'])) + \
              '\n' + \
              ("Температура:" + ' ' + str(data['main']['temp'])) + '\n' + \
              ("Минимальная температура:" + ' ' + str(data['main']['temp_min'])) + '\n' + \
              ("Максимальная температура" + ' ' + str(data['main']['temp_max'])) + '\n'
    bot.send_message(msg.chat.id, content)


def show_result_forecast(data, s_city, msg):
    content1 = ("Прогноз погоды на неделю в городе " + str(s_city) + " :") + '\n'
    bot.send_message(msg.chat.id, content1)
    dateunix = []

    for i in data['list']:
        if (datetime.datetime.fromtimestamp(int(i['dt'])).strftime('%d')) not in dateunix:
            content2 = ''
            dateunix.append(datetime.datetime.fromtimestamp(int(i['dt'])).strftime('%d'))
            content2 = "Дата <" + str(i['dt_txt']) + "> \r\nТемпература <" + str(
                '{0:+3.0f}'.format(i['main']['temp'])) + \
                       "> \r\nПогодные условия <" + str(i['weather'][0]['description']) + "> \r\nСкорость ветра <" + \
                       str(i['wind']['speed']) + "> \r\nВидимость <" + str(i['visibility']) + ">" + \
                       "\n____________________________"
            bot.send_message(msg.chat.id, content2)


def gen_city_choice():
    markup = telebot.types.InlineKeyboardMarkup()
    markup.row_width = 2
    context = ''
    for ev_city in CITIES.keys():
        context += "telebot.types.InlineKeyboardButton(" + str(CITIES.get(ev_city)) + ", callback_data=" + \
                   str(ev_city) + ','

    markup.add(telebot.types.InlineKeyboardButton("Москва", callback_data='1'),
               telebot.types.InlineKeyboardButton("Санкт-Петербург", callback_data='2'),
               telebot.types.InlineKeyboardButton("Казань", callback_data='3'),
               telebot.types.InlineKeyboardButton("Самара", callback_data='4'),
               telebot.types.InlineKeyboardButton("Екатеринбург", callback_data='5'),
               telebot.types.InlineKeyboardButton("Новосибирск", callback_data='6'),
               telebot.types.InlineKeyboardButton("Хабаровск", callback_data='7'),
               telebot.types.InlineKeyboardButton("Владивосток", callback_data='8')
               )
    return markup


bot.polling()
