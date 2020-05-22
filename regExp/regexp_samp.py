import re

"""
match()     文字列の銭湯で正規表現とマッチするか判定
search()    文字列を操作して、正規表現がどこにマッチしているかを調べる
findall()   正規表現にマッチする部分文字列を探し出し、リストとして返す
finditer()  重複しないマッチオブジェクトのイテレータを返す
"""

m = re.match('a.c','abc')
print(m.group())

m = re.search('a.c', 'test abc test abc')
print(m)
print(m.span())
print(m.group())

m = re.findall('a.c', 'test abc test abc')
print(m)

m = re.finditer('a.c', 'test abc test abc')
print([w.group() for w in m])

m = re.match('ab?', 'abb')
print(m)

#\wで英数字or'_'に対応
m = re.match('\w', '_')
print(m)
