from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class TimesVisited(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer)