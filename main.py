#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author  ：huiwentong
@EMAIL   ：wentong.hui@pearlstudio.com
@Date    ：2024/3/13 15:48 
'''
from flask import Flask

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def index():
    print("Welcome")
    return 'Hello World!'

if __name__ == '__main__':
    print('Python')
    app.run(debug=True)
