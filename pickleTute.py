#プログラムを実行し終えたあとも作成したオブジェクトを保存する機能を提供してくれる
#オブジェクトの直列化のため、オブジェクトをファイルに保存できる。→チーム開発とかで役に立つよ
#DBを使わずにjsonオブジェクトを保存したい時にも使える

import pickle

class T(object):
    def __init__(self,name):
        self.name = name

data = {
    'a':[1,2,3],
    'b':('test','test2'),
    'c':{'key':'value'},
    'd':T('test')
}

with open('data.pickle','wb') as f:
    pickle.dump(data,f)

with open('data.pickle','rb') as f:
    data_loaded = pickle.load(f)
    print(type(data_loaded['a']))
    print(type(data_loaded['b']))
    print(type(data_loaded['c']))
    print(type(data_loaded['d']))