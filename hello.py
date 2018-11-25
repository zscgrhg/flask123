# -*- coding: utf-8 -*-
# CLASSWORLDS
# 2018/11/25

from flask import Flask, redirect, url_for

import FaceWork as fw
import FaceWork2 as fw2

app = Flask(__name__)

from flask import render_template
from flask import request

import time


@app.route('/index')
def hello():
    return render_template('hello.html')


@app.route('/index2')
def hello2():
    return render_template('hello2.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        start = time.perf_counter()
        f = request.files['face1']
        f.save('face/face1.png')
        f = request.files['face2']
        f.save('face/face2.png')
        fw.compare("face/face1.png", "face/face2.png")
        end = time.perf_counter()
        print('fw1 executed in %s ms' % ((end - start) * 1000))
    return redirect(url_for('hello'))


@app.route('/upload2', methods=['POST'])
def upload_file2():
    if request.method == 'POST':
        start = time.perf_counter()
        f = request.files['face1']
        f.save('face/face1.png')
        f = request.files['face2']
        f.save('face/face2.png')
        fw2.compare("face/face1.png", "face/face2.png")
        end = time.perf_counter()
        print('fw2 executed in %s ms' % ((end - start) * 1000))
    return redirect(url_for('hello2'))
