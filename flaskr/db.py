from flask import Flask
import flask_sqlalchemys

class Users(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(120), unique=True)

class Post(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(80), unique=False)

