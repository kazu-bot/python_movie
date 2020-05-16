# sqlalchemyを使用することで使用するDBが変わっても柔軟に対応できるようになる。
# オブジェクト指向でSQLが組める。その使い方のサンプル。
import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm

# echo=Trueを追記することで、どんなSQLが書かれたのかすぐわかるようになる。
engine = sqlalchemy.create_engine('sqlite:///:memory:', echo=True)
#mysqlの場合は↓
#engine = sqlalchemy.create_engine('mysql+pymysql:///データベース名', echo=True)

#ベースモデルを作成する。
Base = sqlalchemy.ext.declarative.declarative_base()

#ベースモデルを継承する。
class Person(Base):
    __tablename__ = 'persons'
    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(14)
                             )

#テーブルを作成
#テーブルがない場合CREATE TABLEが実行される。
Base.metadata.create_all(engine)
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

p1 = Person(name='Mike')
session.add(p1)
p2 = Person(name='Nancy')
session.add(p2)
p3 = Person(name='Jun')
session.add(p3)
session.commit()

p4 = session.query(Person).filter_by(name='Mike').first()
p4.name = 'Milchel'
session.add(p4)
session.commit()

p5 = session.query(Person).filter_by(name='Nancy').first()
session.delete(p5)
session.commit()

persons = session.query(Person).all()
for person in persons:
    print(person.id, person.name)
session.close()
