from time import sleep

from dotenv import load_dotenv
import os
from flask import Flask, render_template, request, redirect
import psycopg2

load_dotenv("./.ENV")
db_username = os.getenv('DB_AUTH_USERNAME')
db_passwd = os.getenv('DB_AUTH_PASSWORD')
db_host = os.getenv('DB_AUTH_HOSTNAME')
db_port = os.getenv('DB_AUTH_PORT')
db_name = os.getenv('DB_AUTH_NAME')

app = Flask(__name__)

db = psycopg2.connect(database=db_name,
                      user=db_username,
                      password=db_passwd,
                      host=db_host,
                      port=db_port)

psql = db.cursor()


def get_student_rating():
    try:
        psql.execute("SELECT * FROM public.student WHERE group_numb IN (SELECT numb from public.student_group"
                     " WHERE chair_name = 'КиИБ')"
                     "ORDER BY rating DESC")

        data = psql.fetchall()
        print(data)
        return data


    except:
        print('Fetch error')
        db.rollback()



@app.route("/")
def main_page():
    data = get_student_rating()
    return render_template('table.html', data=data)


get_student_rating()
