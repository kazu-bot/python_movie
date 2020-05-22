import collections

#dict定義
a = {'a':'a', 'c':'c','num':0}
b = {'b':'b','c':'cc'}
c = {'b':'bbb','c':'ccc'}

#aをどんどんアップデートすると、元の内容が書き換わる。
#deepcopyのような値で保存しておく場合は別の変数が必要。それは面倒
print(a)
a.update(b)
print(a)
a.update(c)
print(a)
print('**********************')

a = {'a':'a', 'c':'c','num':0}
b = {'b':'b','c':'cc'}
c = {'b':'bbb','c':'ccc'}
#そこでChainmapを使用。元の値を保存しておける。
m = collections.ChainMap(a,b,c)
print(m)
print('1.{}'.format(m.maps))
#順序を逆に。
m.maps.reverse()
print('2.{}'.format(m.maps))
del m.maps[0]
print('3.{}'.format(m.maps))
#一度順序を逆にしているため最初の'c'が引っかかる
print(m['c'])
m['b'] = 'BBBBBBB'
print(m.maps)

#条件を使用したアップデートも可能。エラーにはならない。
#numに値が０よりも小さい場合は書き換えないようにする
class DeepChainMap(collections.ChainMap):
    def __setitem__(self, key, value):
        for mapping in self.maps:
            if key in mapping:
                if type(mapping[key]) is int and mapping[key] < value:
                    mapping[key] = value
                return
        self.maps[0][key]=value

m = DeepChainMap(a,b,c)
m['num'] = -1
print(m['num'])