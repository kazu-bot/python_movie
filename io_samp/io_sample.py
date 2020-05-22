#ファイルの操作をメモリー上で行える。
#zipファイルの中身を展開せずともメモリ上に展開して内容を取得→削除といったこともできる。
import io

import requests
import zipfile

with open('/tmp/a.txt', 'w') as f:
    f.write('test test')
with open('/tmp/a.txt', 'r') as f:
    print(f.read())

url = ('')

f=io.BytesIO()
r = requests.get(url)
f.write(r.content)

with zipfile.ZipFile(f) as z:
    with z.open('README.txt') as f:
        print(r.read().decode())