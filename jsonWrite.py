#pythonを使ってjsonを書く
import json

j = {
    "employee":
        [
            {"id":111,"name":"Mike"},
            {"id":222,"name":"Nancy"}
        ]
}

print(j)
print("##############")
#ファイルに書き込む時は"dumps"
#python内で使用する時は"dump"
#load時も同様
print(json.dumps(j))
#jsonの場合はwithステートメントを使う
with open('test.json','w') as f:
    json.dump(j,f)
with open('test.json','r') as f:
    json.dump(json.load(f))

