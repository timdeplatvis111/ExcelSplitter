import os, time, flask, string, MySQLdb

from os.path import join, dirname, realpath
from flask import Flask
from flask import Blueprint, render_template, request, redirect, url_for, flash, sessions, session, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import *

#Voor het persoon die, heel misschien ooit, deze code zal vinden en er mee moet werken:
#De code is shit, dat weet ik. Ik ben nog niet echt goed in Python. 
#Als je deze code moet onderhouden en tips voor mij heeft, of gewoon vragen, voeg mij dan toe op: https://steamcommunity.com/id/timdeplatvis111/
#Good luck bij dit bedrijf ouwe, ik vond mijn stage best leuk. 

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['xlsx'])
def allowed_file(filename):
    return '.' in filename and \
    filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

app.config.from_mapping(
    SECRET_KEY = b'5t=759f9$gfdh>f047]8y87^4#5gq8*3nft8503#mgtrhsuooer9',
    UPLOADED_FILES = f'C:/Users/timde/Desktop/KingsofIndigo/Excel/flaskr/files/',
    UPLOADS_PATH = join(dirname(realpath(__file__)), f'C:/Users/timde/Desktop/KingsofIndigo/Excel/flaskr/files/'),
    DEBUG = 'true',
    DEBUG_MODE = 'true',
    FLASK_ENV= 'development',
    conn = MySQLdb.connect(host="localhost",user="root",password="",db="Splitter")
)

conn = MySQLdb.connect(host="localhost",user="root",password="",db="Splitter")
#conn = MySQLdb.connect(host="Timdeplatvis111.mysql.pythonanywhere-services.com",user="Timdeplatvis111",password="CdYudQM75q7DxHh",db="Timdeplatvis111$Splitter")

#Zet de maximum allowed file size naar 16 MB
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

#Zet de debug mode naar true, dit moet op false zijn in de live version
app.config['DEBUG_MODE'] = True

#Zet de enviroment naar development, moet uit in de live version
app.config['FLASK_ENV'] = 'development'

from flaskr import routes

