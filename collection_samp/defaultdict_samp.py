# defaultdict, Counterを使ってみる。

import collections

d = {}
l = ['a', 'a', 'a', 'b', 'b', 'c']

# defaultdictを使用せず、リストの文字がいくつ入ってるか確認する場合
for word in l:
    if word not in d:
        d[word] = 0
    d[word] += 1
print(d)

# dictのsetdefaultを使用して書く場合
d = {}
l = ['a', 'a', 'a', 'b', 'b', 'c']
for word in l:
    d.setdefault(word, 0)
    d[word] += 1
print(d)

# setdefaultを使用する場合
# 宣言時にintを使用する
d = collections.defaultdict(int)
l = ['a', 'a', 'a', 'b', 'b', 'c']
for word in l:
    d[word] += 1
print(d)

# 集合としても使える
d = collections.defaultdict(set)
s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]

for key, value in s:
    d[key].add(value)
# 出力結果
# defaultdict(<class 'set'>, {'red': {1, 3}, 'blue': {2, 4}})
print(d)

# ここまで長々とカウントを行ったが、collections.Counterを使用することで、
# より楽にカウントを行える
l = ['a', 'a', 'a', 'b', 'b', 'c']
c = collections.Counter()
for word in l:
    c[word] += 1
#実行結果：Counter({'a': 3, 'b': 2, 'c': 1})
print(c)
#most_commonを使用すると回数の多いものを表示する。引数の数字分出力も可能
print(c.most_common(1))

