#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author  ：huiwentong
@EMAIL   ：wentong.hui@pearlstudio.com
@Date    ：2024/3/13 15:48 
'''
from flask import Flask, url_for, render_template, request, make_response
from werkzeug.utils import secure_filename

# url_for 是用来做测试的，测试路由中的url地址，一般搭配app.test_request_context来使用

app = Flask(__name__)

@app.route('/arg/<int:id>', methods=['GET'])
def arg(id):
    if id == 1:
        return 'this is id = 1'
    elif id == 2:
        return 'this is id = 2'
    elif id == 3:
        return 'this is id = 3'
    else:
        return f'this id is {id}, and i dont know'

# 也可以使用
# @app.get('/login')
# @app.post('/login')
@app.route('/login', methods=['GET', 'POST'])
def login():
    return 'login'

# 也可以使用这种方式 @app.get('/')
@app.route('/', methods=['GET'])
def index():
    return 'Hello World!'

@app.route('/redirect', methods=['GET'])
def redirect():
    return redirect(url_for('/'))


@app.route('/hello/<name>', methods=['GET'])
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    print('Python')
    with app.test_request_context():
        print(url_for('arg', id=1))
        print(url_for('arg', id=2))
        print(url_for('arg', id=3))
        print(url_for('login', test='/'))
        print(url_for('index'))
    app.run(host="192.168.100.105", debug=True, port=24217)
