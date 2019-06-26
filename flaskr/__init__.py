import os, time, flask, string, MySQLdb, sqlalchemy, flask_bcrypt

from flask_bcrypt import Bcrypt

from os.path import join, dirname, realpath

from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash, sessions, session, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from werkzeug.utils import *

#Voor het persoon die, heel misschien ooit, deze code zal vinden en er mee moet werken:
#De code is shit, dat weet ik. Ik ben nog niet echt goed in Python. 
#Als je deze code moet onderhouden en tips voor mij heeft, of gewoon vragen, voeg mij dan toe op: https://steamcommunity.com/id/timdeplatvis111/
#Good luck bij dit bedrijf, ik vond mijn stage leuk. 

#Als je een ontwikkelaar bent die deze code voor mij reviewed
#Ik weet dat je eigelijk geen globlal variables moet gebruiken in Python, je moet ze declaren in de 'class' 
#Verder is de code redelijk gestructureerd, veel succes tho
#Er is sowieso ook een betere manier om de optie functie te maken

app = Flask(__name__)

#Zet het filetypen naar .xlsx, een standaard Excel formaat. Andre soort Excel bestanden zijn niet supported door issues met openpyxl
ALLOWED_EXTENSIONS = set(['xlsx'])
def allowed_file(filename):
    return '.' in filename and \
    filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

#Instellingen die gebruikt worden voor de hele app
app.config.from_mapping(
    SECRET_KEY = b'5t=759f9$gfdhpf047]8y87^4#5gq8*3nft8503#mgtrhsuooer9',
    UPLOADED_FILES = f'files/',
    UPLOAD_FOLDER = join(dirname(realpath(__file__)), f'files/'),
    DEBUG = 'true',
    DEBUG_MODE = 'true',
    FLASK_ENV= 'development',
)

#Connect naar de MYsql database met flask sqlalchemy
#VERANDER HET PASSWORD, HET PASSWORD IS NU YEET
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:yeet@localhost/splitter'

#Zet de maximum allowed file size naar 16 MB
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

#Zet de debug mode naar true, dit moet op false staan in de live version
app.config['DEBUG_MODE'] = True

#Zet de enviroment naar development, moet uit in de live version
app.config['FLASK_ENV'] = 'development'

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

#Initialseerd de database en bcrypt
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

#Import the routes uit routes.py van de folder flaskr
from flaskr import routes

