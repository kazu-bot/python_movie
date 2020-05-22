import enum

#uniqueでなければならない場合はデコレータを追加
#@enum.unique
#定義をInt型で使用したい場合は「enum.Intenum」でもいける。
class Status(enum.Enum):
    ACTIVE = 1
    RENAME_ACTIVE = 1
    INACTIVE = 2
    RUNNING = 3

class Perm(enum.IntFlag):
    R = 4
    W = 2
    X = 1

print(Perm.R | Perm.W)
print(repr(Perm.R | Perm.W))

print(Status.ACTIVE)
print(repr(Status.ACTIVE))
print(Status.ACTIVE.name)
print(Status.ACTIVE.value)

for s in Status:
    print(s)
    print(type(s))

print(Status(1))

#DBにサーバの情報を入れる場合

db = {
    'stack1':1,
    'stack2':2
}

if Status(db['stack1']) == Status.ACTIVE:
    print('shutdown')
elif Status(db['stack1']) == Status.INACTIVE:
    print('terminate')