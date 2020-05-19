#json方式でDBに保存できる
#./data/dbフォルダを作成し、,mongodbを起動
#mongod --dbpath ./data/db
#普通のSQLと同じような操作性は無いが、あまりアップデートを行わないようなデータについては
# mongoDBを使用した方が早く処理が行えることが多い。

import datetime
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['test_database']

stack1 = {
    'name':'customer1',
    'pip':['python','java','go'],
    'info':{'os':'mac'},
    'data': datetime.datetime.utcnow()
}

stack2 = {
    'name':'customer2',
    'pip':['python','java'],
    'info':{'os':'win'},
    'data': datetime.datetime.utcnow()
}

#DB作成しているイメージ
db_stacks = db.stacks
stack_id = db_stacks.insert_one(stack1).inserted_id
print(stack_id,type(stack_id))
print('#############')
print(db_stacks.find_one({'_id':stack_id}))

now = datetime.datetime.utcnow()
for stack in db_stacks.find({'date':{'$gt':now}}):
    print(stack)

#一応updateやdelete等の操作も可能
db_stacks.find_one_and_update(
    {'name':'customer1'},{'$set':{'name':'YYY'}}
)
print((db_stacks.find_one({'name':'YYY'})))

#delete
db_stacks.delete_one({'name':'YYY'})
print(db_stacks.find_one({'name':'YYY'}))