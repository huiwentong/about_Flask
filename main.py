#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author  ：huiwentong
@EMAIL   ：wentong.hui@pearlstudio.com
@Date    ：2024/3/13 15:48 
'''
from flask import Flask, url_for, render_template, request, make_response, abort, redirect, session
from werkzeug.utils import secure_filename
import secrets

# url_for 是用来做测试的，测试路由中的url地址，一般搭配app.test_request_context来使用

app = Flask(__name__)
app.secret_key = secrets.token_hex() # 如果想使用session， 首先必须先生成一个secrets_key

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

@app.route('/abort')
def abort_test():
    abort(401)

# 也可以使用这种方式 @app.get('/')
@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('hello', name='redirect'))

@app.route('/redirect', methods=['GET'])
def redirect_test():
    return redirect(url_for('abort_test'))

@app.errorhandler(404)
def page_not_found(e):
    return make_response(render_template('page_not_found.html'), 404)

@app.route('/hello/<name>', methods=['GET'])
def hello(name=None):
    return render_template('hello.html', name=name)

#________________以下是session使用案例________________

@app.route('/index', methods=['GET'])
def index_session():
    if 'username' in session:
        return 'Logged in as %s' % session['username']
    return 'you are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index_session'))
    return '''
        <form method="POST">
            <input type="text" name="username">
            <input type="submit" value=login>
        </form>
    '''

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('username', None)
    return redirect(url_for('index_session'))


if __name__ == '__main__':
    print('Python')
    with app.test_request_context():
        print(url_for('arg', id=1))
        print(url_for('arg', id=2))
        print(url_for('arg', id=3))
        print(url_for('login', test='/'))
        print(url_for('hello', name="huiwentong"))
    app.run(host="192.168.100.105", debug=True, port=24217)
