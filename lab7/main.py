import telebot
import os
from dotenv import load_dotenv
import psycopg2

load_dotenv("./.env")
db_env = {
    "name": os.getenv('PSQL_DB_NAME'),
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
        db = psycopg2.connect(database=db_env_keys.name,
                              user=db_env_keys.user,
                              password=db_env_keys.password,
                              host=db_env_keys.hostname,
                              port=db_env_keys.port)
    except Exception as e:
        print("Startup of DB Error! Error: ", e)
        return False

def Service (db_env_keys,tg_key):
    StartBotService(tg_key)
    StartDBService(db_env_keys)

def bot_session(bot):
    bot.infinity_polling()


Service(db_env,telegram_key)