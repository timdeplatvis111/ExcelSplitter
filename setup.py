        """
        uploaded_files = request.files.getlist("file[]")
        file = request.files['file']
        filenames = []

        for file in uploaded_files:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOADED_FILES'], filename))
            print (filenames)

        print (uploaded_files)
        return ""
        """

            @app.route('/upload', methods=["POST"])
    def upload():
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('index'))
            print (uploaded_files)
            print (filenames)
        return render_template('index.html')
    return app