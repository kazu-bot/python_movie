## Pythonのtips

+ pythonコードスタイルをチェックしてくれるツールのインストール
```cmake:pep8&nbsp;install&nbsp;コマンド.py
pip install pep8
```
```cmake:flake8&nbsp;install&nbsp;コマンド
pip install flake8
```

+ 暗黙ルール<br>
  1.セミコロンで改行はしない<br>
  2.1行は80文字以内

+ forループ時はジェネレータを使用すると良いよ
```python:ジェネレータの例
####ジェネレータ無し
def t():
	for i in range(10)
		num.append(i)
	return num
for i in t():
	print(i)
####ジェネレータ使用
def t():
	for i in range(10)
		yield i
```
+ 抽象クラス
継承した先がメソッドの作成を必ず行うようにする(まあJavaと一緒)
```python:抽象クラス
import abc
class Person(metaclass = abc.ABC.Meta):
	def __init__(self, age = 1):
		self.age = age

	@abc.abstractmethod
	def drive(self):
		pass
```

+ loggingフィルタ
ログに出力したくない内容を記載することで出力を制御できる
```python
#passwordが記載されたログを出力したくない
class NoPassFilter(logging.Filter):
	def filter(self, record):
		log_message = record.getMessage()
		return 'password' not in log_message
logger = logger.getLogger(__name__)
logger.addFilter(NoPassFilter()) #ココ
logger.info('from main')
logger.info('from main password = "test"')
```

+ memcached
memcachedは高性能な分散メモリキャッシュサーバ
通常，データベースへの問い合わせ結果を一時的にキャッシュすることで，データベースへのアクセス回数を減らし，動的なウェブアプリケーションの高速化やスケーラビリティの向上のために利用されています

+ JSON
 JSONとはJavaScript Object Notationの略で、XMLなどと同様のテキストベースのデータフォーマット。
 XMLと比べると簡潔に構造化されたデータを記述することができるため、記述が容易で人間が理解しやすい。
 Ajax(Webブラウザ上で動作するJavaScriptでサーバからXMLデータを取得し、取得したデータをDHTMLを活用してコンテンツに動的に反映するという手法)でのデータ交換フォーマットとして広く利用されるようになった。

+ neo4j
グラフデータベースを使用する。履歴系管理とか使えそうだな。
グラフ構造を持ったデータの保存、探索、集計に最適化されたデータベース。
RDBでは幾つものも関連テーブルを用意してjoin後集計する必要があった人間関係を示すソーシャルグラフやECサイトにおける購入履歴等で利用されている。
```neo4j:command例
CREATE(kazu:Person{name:"kazu"})
MATCH (kazu:Person(name:"kazu"))
CREATE(kazu)-[like:LIKE]->(python:Language{name:"Python"})
RETURN kazu,like,python
```

+ deque  
deque(デキュー)とは、double ended queueの略で、queueの両端からappend/popを行えるようにしたもの  
リストでも同様の操作を実現できるが、dequeのほうがより高速に動作させられる