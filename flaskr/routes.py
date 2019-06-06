import os, time, flask, string, MySQLdb, openpyxl, wtforms, jinja2

from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash, sessions, session, send_from_directory, send_file

from flaskr import app, allowed_file, flask_bcrypt, db, bcrypt

from os.path import join, dirname, realpath

from flask_sqlalchemy import SQLAlchemy

from openpyxl import load_workbook

from werkzeug.utils import *
from werkzeug.wrappers import BaseRequest
from werkzeug.wsgi import responder
from werkzeug.exceptions import HTTPException, NotFound

from forms import RegistrationForm, LoginForm, PostForm
from flaskr.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

#Variables voor de exception catchers, moeten eerst een value hebben for some reason
a, b, c, d = '', '', '', ''

#TODO: Dit even uncommenten nog  
#{{ form.remember(class="form-check-input") }}
#{{ form.remember.label(class="form-check-label") }} 

@app.route('/', methods=['GET', 'POST'])
def index():
    registerform = RegistrationForm()
    if registerform.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(registerform.password.data).decode('utf-8')
        user = User(username=registerform.username.data, email=registerform.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('index'))

    loginform = LoginForm()
    if loginform.validate_on_submit():
        user = User.query.filter_by(email=loginform.email.data).first()
        if user and bcrypt.check_password_hash(user.password, loginform.password.data):
            login_user(user, remember=loginform.remember.data)
            #next_page = request.args.get('next')
            #return redirect(next_page) if next_page else redirect(url_for('index'))
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    """
    accountform = AccountForm()
    if accountform.validate_on_submit():
        #if accountform.picture.data:
        #    picture_file = save_picture(accountform.picture.data)
        #    current_user.image_file = picture_file
        current_user.username = accountform.username.data
        current_user.email = accountform.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('index'))
    """

    if current_user.is_authenticated:
        userfolder = current_user.username
        converteduserfiles = []
        userfiles = []

        path = f'files/{userfolder}/'

        if (os.path.exists(f'files/{userfolder}/converted')):
            pathtoconverted = f'files/{userfolder}/converted'
        else:
            os.mkdir(f'files/{userfolder}')
            os.mkdir(f'files/{userfolder}/converted')
            pathtoconverted = f'files/{userfolder}/converted'

        for filename in os.listdir(path):
            userfiles.append(filename)

        for filename in os.listdir(pathtoconverted):
            converteduserfiles.append(filename)
    else:
        filename = ''
        path = ''
        userfiles = '', ''
        converteduserfiles = ''
        pathtoconverted = ''
        session['filename'] = filename
        session['path'] = path
        session['userfiles[]'] = userfiles
        session['converteduserfiles[]'] = converteduserfiles
        session['pathtoconverted'] = pathtoconverted

    session['filename'] = filename
    session['path'] = path
    session['userfiles[]'] = userfiles
    session['converteduserfiles[]'] = converteduserfiles
    session['pathtoconverted'] = pathtoconverted

    #elif request.method == 'GET':
        #if current_user.is_authenticated:
            #accountform.username.data = current_user.username
            #accountform.email.data = current_user.email
        #else:
            #return redirect(url_for('index'))
            #return render_template('index.html', title='Account', image_file=image_file, accountform=accountform, loginform=loginform, registerform=registerform)
    #image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    #return render_template('index.html', title='Account', image_file=image_file, accountform=accountform, loginform=loginform, registerform=registerform)
    #return render_template('index.html', title='Account', accountform=accountform, loginform=loginform, registerform=registerform)

    postform = PostForm()
    if postform.validate_on_submit():
        post = Post(title=postform.title.data, content=postform.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('index'))
    
    posts = Post.query.all()

    environment = jinja2.Environment(os)
    environment.filters['os'] = os

    #return render_template('index.html', title='Account', accountform=accountform, loginform=loginform, registerform=registerform, postform=postform, os=os)
    return render_template('index.html', title='Account', loginform=loginform, registerform=registerform, postform=postform, posts=posts, userfiles=session['userfiles[]'], path=session['path'], filename=session['filename'], pathtoconverted=session['pathtoconverted'], converteduserfiles=session['converteduserfiles[]'], os=os)
    #return render_template('index.html', title='Account', pathtoconverted=session['pathtoconverted'], converteduserfiles=session['converteduserfiles[]'], userfiles=session['userfiles[]'], path=session['path'], filename=session['filename'], os=os, accountform=accountform, loginform=loginform, registerform=registerform, postform=postform, posts=posts)

@app.route('/files', methods=['GET', 'POST'])
def files():
    filename = session.get('filename')
    path = session.get('path')
    userfiles = session.get('userfiles[]')

    for index, filename in enumerate(userfiles):
        print(index)
    return send_from_directory(f'../{path}', userfiles[index], as_attachment=True)

@app.route('/files2', methods=['GET', 'POST'])
def files2():
    filename = session.get('filename')
    converteduserfiles = session.get('converteduserfiles[]')
    pathtoconverted = session.get('pathtoconverted')

    for index, filename in enumerate(converteduserfiles):
        print(index)
    return send_from_directory(f'../{pathtoconverted}', converteduserfiles[index], as_attachment=True)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    #Dit hele ding zit in een try catch systeem om elke soort exploit te voorkomen, ik wil geen random errors op de website. 
    try: 
        #Pakt de files uit de form
        request.files['uploadedfiles']

        userfolder = current_user.username

        #Maakt een list van de 2 geuploade files, zodat we er later door heen kunnen loopen 
        yeet = request.files.getlist('uploadedfiles')
        filenamen = []

        #Loopt door de filelist heen
        for file in yeet:     
            files = request.files.to_dict()
            filename = secure_filename(file.filename)
            filenamen.append(filename)

            #Checkt of het type file klopt, er mogen alleen .xlsx files geupload worden
            if file and allowed_file(filename):
                if (os.path.exists(f'files/{userfolder}')):
                    file.save(f'files/{userfolder}/{filename}')
                else:
                    os.makedirs(f'files/{userfolder}')
                    file.save(f'files/{userfolder}/{filename}')
            else:
                fileerror= 'fuck'
                flash('yeet', 'fileerror')
                return render_template('index.html', fileerror=fileerror)

        if len(filenamen) is not 2:
            flash('Please upload 2 Excel files', 'error')
            return render_template('convert.html', error=error)    
        else:
            #Zet de filenamen array in de session voor later gebruik 
            session['filenamen[]'] = filenamen
        return render_template('convert.html', filenamen=session['filenamen[]'])    

    except KeyError as d:
        flash(str(d), 'error')
        return redirect("/")
        return render_template('index.html')

    except:
        return redirect("/")
        return render_template('index.html', error=error)

@app.route('/convert', methods=['GET', 'POST'])
def convert():
    try:
        userfolder = current_user.username
        #Loopt door het alfabet heen en assigned zo een nummer naar elk letter, A = 1, B = 2, etc
        #Dit is nog een probleem, dit gaat alleen van column A tot X
        values = dict()
        for index, letter in enumerate(string.ascii_lowercase):
            values[index] = letter
            print(values[index])

        #Pakt de filenamen array uit de session
        filenamen = session.get('filenamen[]')

        #Split de array in 2 variabelen voor later gebruik
        filenaam1 = filenamen[0]
        filenaam2 = filenamen[1]

        #column1 = de eerste column die je wilt matchen uit de form (filenaam1)
        #column2 = de tweede column die je wilt matchen uit de form (filenaam2)
        column1 = request.form['column1']
        column2 = request.form['column2']

        #option = de file waarvan je de values wilt kopieren uit de form
        option = request.form['option']

        #column1copy = de column waarvan je de values wilt kopieren uit de form
        #column2copy = de column waar naar je de values wilt kopieren uit de form
        column1copy = request.form['column1copy']
        column2copy = request.form['column2copy']

        #Zet beide workbooks als de active workbooks, dit moet om het te kunnen gebruiken in OpenpyXL
        workbook1 = load_workbook(filename=(f"files/{userfolder}/{filenaam1}"))
        sheet1 = workbook1.active

        workbook2 = load_workbook(filename=(f"files/{userfolder}/{filenaam2}"))
        sheet2 = workbook2.active

        #Convert deze variabelen naar integrers voor later gebruik
        column1copy = int(column1copy)
        column2copy = int(column2copy)

        column1 = int(column1)
        column2 = int(column2)

        sheet1column = values[column1]
        sheet2column = values[column2]

        #Deze code looped door de opgegeven column in bestand 1 (for cell in sheet1[sheet1column]:I = cell.row) en pakt de value van de eerste row in de opgegeven columns
        #sheet1value = sheet1.cell(row=I, column=column1).value, I is gelijk aan de huidige cell's row
        #Dan gaat het naar de 2e for statement, hier gebeurt hetzelfde alleen checkt het nu of de de gevonden value gelijk is aan de value in het eerste bestand

        print (option)
        t = time.process_time()
        loops = 0

        if option == 'file0':
            filename = filenaam1

            for cell in sheet1[sheet1column]:
                filename = filenaam2
                I = cell.row
                sheet1value = sheet1.cell(row=I, column=column1).value

                for cell in sheet2[sheet2column]:
                    E = cell.row
                    sheet2value = sheet2.cell(row=E, column=column2).value

                    if sheet1value == sheet2value:
                        sheet1copyvalue = sheet1.cell(row=I, column=column1copy).value
                        sheet2.cell(row=E, column=column2copy, value=sheet1copyvalue)
                        loops +=1
                    else:
                        loops +=1

        elif option == 'file1':
            filename = filenaam2

            for cell in sheet2[sheet2column]:
                I = cell.row
                sheet2value = sheet2.cell(row=I, column=column2).value

                for cell in sheet1[sheet1column]:
                    E = cell.row
                    sheet1value = sheet1.cell(row=E, column=column1).value

                    if sheet2value == sheet1value:
                        sheet1copyvalue = sheet2.cell(row=I, column=column1copy).value
                        sheet1.cell(row=E, column=column2copy, value=sheet1copyvalue)
                        loops +=1
                    else:
                        loops +=1

        if option == 'file0':
            if (os.path.exists(f'files/{userfolder}')):
                workbook1.save(f'files/{userfolder}/{filenaam1}')
                workbook2.save(f'files/{userfolder}/{filenaam2}')
            else:
                os.makedirs(f'files/{userfolder}')
                workbook1.save(f'files/{userfolder}/{filenaam1}')
                workbook2.save(f'files/{userfolder}/{filenaam2}')

        elif option == 'file1':
            if (os.path.exists(f'files/{userfolder}')):
                workbook1.save(f'files/{userfolder}/{filenaam1}')
                workbook2.save(f'files/{userfolder}/{filenaam2}')
            else:
                os.makedirs(f'files/{userfolder}')
                workbook1.save(f'files/{userfolder}/{filenaam1}')
                workbook2.save(f'files/{userfolder}/{filenaam2}')

        #Measured hoe lang het duurde voor de code om door de logica te gaan
        elapsed_time = time.process_time() - t

        #Dit zorgt er voor dat de time en het aantal loops gerendered worden in de template 
        flash(elapsed_time, 'time')
        flash(loops, 'loops')

        if (os.path.exists(f'files/{userfolder}/converted')):
            print('YEETICUS')
        else:
            os.mkdir(f'files/{userfolder}/converted')

        if option == 'file0':
            workbook2.save(f'files/{userfolder}/converted/{filenaam2}')
            return send_from_directory(f'../files/{userfolder}', filenaam2, as_attachment=True)
        elif option == 'file1':
            workbook1.save(f'files/{userfolder}/converted/{filenaam1}')
            return send_from_directory(f'../files/{userfolder}', filenaam1, as_attachment=True)

        session.pop('_flashes', None) 

    #Dit zijn alle exceptions voor verschillende errors, meeste errors zouden niet kunnen gebeuren, maar staan er toch just to be sure
    except KeyError as a:
        return redirect("/")
        return render_template('index.html')
        session.pop('_flashes', None)

    except NameError as b:
        flash(str(b), 'error')
        return redirect("/")
        return render_template('index.html', error=error)
        session.pop('_flashes', None)

    except ValueError as c:
        flash(str(c), 'error')
        return redirect("/")
        return render_template('index.html', error=error)
        session.pop('_flashes', None)

    except TypeError as f:
        flash(str(f), 'error')
        return redirect("/")
        return render_template('index.html', error=error)
        session.pop('_flashes', None)

    except:
        message = 'This is never supposed to happen, Please contact the administrator if it does'
        flash(str(message), 'error')
        return redirect("/")
        return render_template('index.html', error=error)
        session.pop('_flashes', None)


