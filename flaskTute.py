#pythonで使用するウェブアプリケーションフレームワーク
#これを覚えておけばDjangoにも移行しやすい。
from flask import Flask, g
from flask import render_template
from flask import request
from flask import Response


#DBにアクセスしてみる
import sqlite3

app = Flask(__name__)

#DB接続
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g,_database = sqlite3.connect('test_sqlite.db')
    return db

#セッションの最後にDBをcloseする。
#最後に行う処理を「@app.teardown_appcontext」でデコレーションしてやる。
@app.teardown_appcontext
def close_connection(exeption):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/employee', methods=['POST', 'PUT', 'DELETE'])
@app.route('/employee/<name>', methods=['GET'])
def employee(name=None):
    db = get_db()
    curs = db.cursor()
    curs.execute(
        'CREATE TABLE IF NOT EXISTS persons( '
        'id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)'
    )
    db.commit()

    name = request.values.get('name',name)
    if request.method =='GET':
        curs.execute('SELECT * FROM persons WHERE name = "{}"'.format(name))
        person = curs.fetchone()
        if not person:
            return "NO", 404
        user_id, name = person
        return '{}:{}'.format(user_id,name), 200

    if request.method == 'POST':
        curs.execute('INSERT INTO persons(name) values("{}")'.format(name))
        db.commit()
        return 'created {}'.format(name), 201

    if request.method == 'PUT':
        new_name = request.values['new_name']
        curs.execute('DELETE persons set name = "{}" WHERE name = "{}"'.format(
            new_name, name
        ))
        db.commit()
        return 'update {}:{}'.format(name,new_name),200

    if request.method == 'DELETE':
        curs.execute('DELETE from persons WHERE name = "{}"'.format(name))
        db.commit()
        return 'deleted {}'.format(),200


#ウェブページの最初のスラッシュが来たら値を返す
@app.route('/')
def hello_world():
    return 'top'

#http://127.0.0.1:5000/hello/kazu
@app.route('/hello/')
@app.route('/hello/<username>')
def hello_world2(username=None):
    #return 'hello world! {}'.format(username)
    #毎回書くのも面倒なのでテンプレート化する。
    #ファイルは./templates/hello.htmlを使用
    return render_template('hello.html', username=username)

#下記でアクセスを受け取って値を返す
#POST,PUT,DELETEに対応
@app.route('/post', methods=['POST','PUT','DELETE'])
def show_post():
    return str('こんにちは。{}さん'.format(request.values['username']))
    #return str(request.values['username'])

# @app.route('/hello/')
# def hello_world2(username):
#     return 'hello world!'

def main():
    app.debug = True
    app.run()
    #デフォルト設定でhost='127.0.0.1', port=5000

if __name__ == '__main__':
    main()