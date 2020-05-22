#正規表現と置換
import re

s = 'My name is ... Mike'
print(s.split())

p = re.compile(r'\W+')
print((p.split(s)))

p = re.compile('(blue|white|red)')
print(p.sub('color', 'blue socks and red shoes'))
print(p.sub('color', 'blue socks and red shoes', count=1))
print(p.subn('color', 'blue socks and red shoes'))

def hexrepl(match):
    value = int(match.group())
    return hex(value)

#正規表現にかかった場合、関数を呼び出すとかもできる。
p = re.compile((r'\d'))
print(p.sub(hexrepl, '12345 55 66 test test2'))