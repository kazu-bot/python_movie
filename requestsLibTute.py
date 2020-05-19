#サードパーティライブラリーの「requests」を使用する。
#xml,jsonの書き方をやってきたが、これを使用することにより簡略化が可能
import  requests

payload = {'key1':'value1','key2':'value2'}

#urllibTuteと見比べるとgetもこんなに簡単
r = requests.get('http://httpbin.org/get',params=payload, timeout=1)
#postの際もこのような書き方でOK
#put,postも同じ書き方すればOK
#r = requests.post('http://httpbin.org/post',data=payload)

print(r.status_code)
print(r.text)
print(r.json())