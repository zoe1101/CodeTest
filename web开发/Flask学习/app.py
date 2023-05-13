from flask import Flask, redirect, url_for, request

app = Flask(__name__)  # 实例化


@app.route('/')  # 注册路由
def index():  # 视图
    return '<h1>Hello, World!</h1>'


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


if __name__ == '__main__':
    app.run(debug=True)
