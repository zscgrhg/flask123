# -*- coding: utf-8 -*-
# CLASSWORLDS
# 2018/11/25

from flask import Flask, redirect, url_for
from werkzeug.utils import secure_filename

import FaceWork as fw
import FaceWork2 as fw2

app = Flask(__name__)

from flask import render_template
from flask import request

import time


@app.route('/index')
def hello(matrix=[]):
    return render_template('hello.html', matrix=matrix)


@app.route('/index2')
def hello2():
    return render_template('hello2.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        start = time.perf_counter()
        f1 = request.files['face1']
        name1 = 'static/face/' + secure_filename(f1.filename)
        f1.save(name1)
        f2 = request.files['face2']
        name2 = 'static/face/' + secure_filename(f2.filename)
        f2.save(name2)
        retmatrix = fw.compare(name1, name2)
        end = time.perf_counter()
        print('fw1 executed in %s ms' % ((end - start) * 1000))
        print(retmatrix)
        return render_template('hello.html', matrix=retmatrix)


@app.route('/save', methods=['POST'])
def save():
    if request.method == 'POST':
        start = time.perf_counter()
        face = request.files['face']
        simpleName = secure_filename(face.filename)
        fileName = 'static/face/' + simpleName
        face.save(fileName)
        fw.save(fileName, simpleName)
        end = time.perf_counter()
        print('save executed in %s ms' % ((end - start) * 1000))

        return render_template('hello.html')

@app.route('/upload2', methods=['POST'])
def upload_file2():
    if request.method == 'POST':
        start = time.perf_counter()
        f = request.files['face1']
        f.save('static/face/face1.png')
        f = request.files['face2']
        f.save('static/face/face2.png')
        fw2.compare("static/face/face1.png", "static/face/face2.png")
        end = time.perf_counter()
        print('fw2 executed in %s ms' % ((end - start) * 1000))
    return redirect(url_for('hello2'))
