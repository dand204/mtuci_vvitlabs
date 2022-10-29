import requests
from dotenv import load_dotenv
import os
from flask import Flask, render_template, request
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


@app.route("/")
def main_page():
    return render_template('main_page.html')


@app.route('/login/', methods=['GET'])
def index():
    return render_template('login.html')


@app.route('/login/', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    try:
        psql.execute("SELECT * FROM service.users WHERE login=%s AND password=%s", (str(username), str(password)))
        records = list(psql.fetchall())
        return render_template('account.html', full_name=records[0][1], username=username, password=password)
    except IndexError:
        if username == password == '':
            return render_template('error_authorization.html', blankLogin=True)
        else:
            return render_template('error_authorization.html')
