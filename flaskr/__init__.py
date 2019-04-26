import os
from os.path import join, dirname, realpath
import flask
from flask import Flask
from flask import Blueprint, render_template, request, redirect, url_for, flash, sessions
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import *

def create_app():
    # create and configure the app
    #app = Flask(__name__, instance_relative_config=True)
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY='5t759f9$gfdhf0478y87^4#5gq8*3nft8503#mgtrhsuooer9',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
        UPLOADED_FILES = 'files/',
        UPLOADS_PATH = join(dirname(realpath(__file__)), 'files/')
    )

    ALLOWED_EXTENSIONS = set(['xlsx'])
    def allowed_file(filename):
        return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/upload', methods=['GET', 'POST'])
    def upload():
        if request.method == 'POST':
            # check if the post request has the file part
            print ('Geyeet')
            if 'file' not in request.files:
                flash('No file part')
                return render_template('index.html')
            file = request.files['file']

            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                #file.save('/files/' filename)
                file.save(os.path.join(app.config['UPLOADS_PATH'], filename))
                #return redirect(url_for('uploaded_file', filename=filename))
                return render_template('index.html')
            else:
                flash('Filetype not allowed, please submit a .xlsx file')
                return render_template('index.html')
        else:
            print ('Geen post?!')
            return render_template('error.html')
    return app


