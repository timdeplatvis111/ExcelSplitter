import os, time, flask, string, MySQLdb

from os.path import join, dirname, realpath
from flask import Flask
from flask import Blueprint, render_template, request, redirect, url_for, flash, sessions, session, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import *
from flask_mysqldb import MySQL
from flaskr import excelreplacer

def create_app(test_config=None):
    app = Flask(__name__)

    #Configuration settings voor app
    app.config.from_mapping(
    #Super secret key, randomly generated door Timbot
    SECRET_KEY = b'5t759f9$gfdhf0478y87^4#5gq8*3nft8503#mgtrhsuooer9',

    #Uploadpath waar files opgeslagen worden voor gebruik in Excel
    #UPLOADED_FILES = '/files/',
    #UPLOADS_PATH = join(dirname(realpath(__file__)), '/files/'),
    DEBUG = 'true',
    DEBUG_MODE = 'true',
    FLASK_ENV= 'development',
    )

    #Database stuff
    conn = MySQLdb.connect(host="Timdeplatvis111.mysql.pythonanywhere-services.com",user="Timdeplatvis111",password="CdYudQM75q7DxHh",db="Timdeplatvis111$Splitter")

    #Zet de maximum allowed file size naar 16 MB
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

    #db.init_app(app)
    #mysql = MySQL(app)

    app.register_blueprint(excelreplacer.bp)

    port = int(os.environ.get("PORT", 5000))
    return app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)