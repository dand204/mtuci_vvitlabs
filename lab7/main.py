import datetime

import telebot
import os
from dotenv import load_dotenv
import psycopg2
from telebot import types

load_dotenv("./.env")
db_env = {
    "database": os.getenv('PSQL_DB_NAME'),
    "user": os.getenv('PSQL_DB_USERNAME'),
    "password": os.getenv('PSQL_DB_PASSWORD'),
    "hostname": os.getenv('PSQL_DB_HOST'),
    "port": os.getenv('PSQL_DB_PORT')}
telegram_key = os.getenv('TELEGRAM_API_KEY')


def StartBotService(tg_key):
    try:
        bot = telebot.TeleBot(tg_key)
        return bot
    except Exception as e:
        print("Telegram bot is not started! ")
        exit()


def StartDBService(db_env_keys):
    try:
        db = psycopg2.connect(database=db_env_keys.get("database"),
                              user=db_env_keys.get("user"),
                              password=db_env_keys.get("password"),
                              host=db_env_keys.get("hostname"),
                              port=db_env_keys.get("port"))
        psql = db.cursor()
        return psql
    except Exception as e:
        print("Startup of DB Error! Error: ", e)
        return False


def BotHandler(bot, psql):
    @bot.message_handler(commands=['start'])
    def start(message):
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.row("На Cегодня", "На Завтра")
        keyboard.row("На Неделю", "На Следующую Неделю")
        keyboard.row("О Боте")
        bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)

    @bot.message_handler(commands=['help'])
    def AnswerHelpCommand(message):
        bot.send_message(message.chat.id, 'Я умею...')

    @bot.message_handler(content_types=['text'])
    def AnswerWith(message):
        if message.text == "О Боте":
            bot.send_message(message.chat.id, 'Тогда тебе сюда - https://mtuci.ru/')
        if message.text == "На Cегодня":
            RaspHandler(bot, psql, message, (datetime.date.today()))
        if message.text == "На Завтра":
            RaspHandler(bot, psql, message, (datetime.date.today() + datetime.timedelta(days=1)))
        if message.text == "На Неделю":
            today = datetime.date.today()
            arg = [today + datetime.timedelta(days=i) for i in range(0 - today.weekday(), 7 - today.weekday())]
            RaspHandler(bot, psql, message, arg)
        if message.text == "На Следующую Неделю":
            today = datetime.date.today()
            pl7 = today + datetime.timedelta(days=7)
            arg = [pl7 + datetime.timedelta(days=i) for i in range(0 - pl7.weekday(), 7 - pl7.weekday())]
            RaspHandler(bot, psql, message, arg)


def RaspHandler(bot, psql, msgpool, target):
    flag = (type(target) is list)

    date_period = [target]

    print(date_period)
    try:
        if not flag:
            psql.execute("SELECT * FROM public.timetable WHERE date=%s ORDER BY pair_numb;", date_period)
        else:
            psql.execute("SELECT * FROM public.timetable WHERE date = ANY(%s) ORDER BY (date, pair_numb)", date_period)

        records = list(psql.fetchall())
        print(records)
    except Exception as e:
        print("Cannot execute data\n", e)
    msg_buffer = ''
    for i in range(len(records)):
        msg_buffer += str(records[i][2]) + ". " + str(records[i][1]) + \
                      "\n    " + str(records[i][5]) + \
                      "\n    Кабинет " + str(records[i][3]) + " " + str(records[i][4] + "\n\n")
    msg = "Расписание на " + str(datetime.datetime.now())[:10] + ":\n" + msg_buffer
    bot.send_message(msgpool.chat.id, msg)


def Service(db_env_keys, tg_key):
    db_cursor = StartDBService(db_env_keys)
    bot_pool = StartBotService(tg_key)
    BotHandler(bot_pool, db_cursor)
    bot_pool.infinity_polling()


Service(db_env, telegram_key)
