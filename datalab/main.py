from flask import Flask, request, redirect, url_for, render_template, flash, Markup
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
conf = dict(
    DEBUG=True,
    SECRET_KEY='dev!',
    SQLALCHEMY_DATABASE_URI='sqlite:///coins.db'
)
app.config.from_envvar('COIN_COUNTER_SETTINGS')
app.config.update(conf)

db = SQLAlchemy(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/acquire')
def got_coin():
    redirect(url_for('index.html'))
