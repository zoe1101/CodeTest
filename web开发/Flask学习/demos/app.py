import os

from flask import Flask, redirect, url_for, request
import flask
app = Flask(__name__)  # 实例化


@app.route('/')  # 注册路由
def index():  # 视图
    return '<h1>Hello, World!</h1>'


# 为视图绑定多个URL
@app.route('/hi')
@app.route('/hello')
def say_hello():
    return '<h1>Hello, Flask!</h1>'


# 动态URL
@app.route('/greet', defaults={'name': 'Programmer'})  # 设置URL变量的默认值
@app.route('/greet/<name>') # url示例：/greet/foo
def greet(name):
    return '<h1>Hello, %s!</h1>' % name


if __name__ == '__main__':
    # app.run(debug=True) # 旧的启动开发服务器的方式是使用app.run（ ） 方法， 目前已不推荐使用
    os.system('flask run')  # 从当前目录寻找app.py和wsgi.py模块， 并从中寻找名为app或application的程序实例;从环境变量FLASK_APP对应的值寻找名为app或application的程序实例,
