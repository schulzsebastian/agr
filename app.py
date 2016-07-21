#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
from script import *

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './files'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('map', filename=filename))
        else:
            return redirect(url_for('index'))


@app.route('/map', methods=['GET'])
def map():
    file = request.args['filename']
    if not file:
        return redirect(url_for('index'))
    data = ''
    # data = image_to_text(app.config['UPLOAD_FOLDER'] + '/' + file)
    return render_template('text.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
