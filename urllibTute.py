"""
REST

HTTPメソッドクライアントが行いたい処理をサーバに伝える

GET     データの参照
POST    データの新規登録
PUT     データの更新
DELETE  データの削除
"""

import urllib.request
import json

# url = 'http://httpbin.org/get'
payload = {'key1': 'value1', 'key2': 'value2'}

# GETでパラメータを送る場合は下記のように書く必要がある。
url = 'http://httpbin.org/get' + '?' + urllib.parse.urlencode(payload)
print(url)

with urllib.request.urlopen(url) as f:
    r = json.loads(f.read().decode('utf-8'))
    print(r, type(r))

# POSTを使用してURLを読み取られない値にする
payload = json.dumps(payload).encode('utf-8')
req = urllib.request.Request(
    'http://httpbin.org/post', data=payload, method='POST'
)

with urllib.request.urlopen(req) as f:
    print(json.loads(f.read().decode('utf-8')))

#PUTとDELETE、書き方は上記とほぼ同じ
req = urllib.request.Request(
    'http://httpbin.org/put', data=payload, method='POST'
)

with urllib.request.urlopen(req) as f:
    print(json.loads(f.read().decode('utf-8')))
req = urllib.request.Request(
    'http://httpbin.org/delete', data=payload, method='POST'
)

with urllib.request.urlopen(req) as f:
    print(json.loads(f.read().decode('utf-8')))
