from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__app__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coins.db'
db = SQLAlchemy(app)


class Coin(db.Model):
    __tablename__='coins'

    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String)
    release_date = db.Column(db.String)
    description = db.Column(db.String)
    img_url = db.Column(db.String)
    possessed = db.Column(db.Boolean)
