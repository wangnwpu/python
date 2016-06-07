#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_get():
    return render_template('response.html', method='GET', headers=request.headers, args=request.args);

@app.route('/', methods=['POST'])
def home_post():
    return render_template('response.html', method='POST', headers=request.headers, body=request.form)

if __name__ == '__main__':
    app.run(host="127.0.0.1",port=5000)