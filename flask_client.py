#flaskのクライアント側テスト
import requests


r = requests.get(
    'http://127.0.0.1:5000/employee/kazu'
)
print(r.text)

r = requests.post(
    'http://127.0.0.1:5000/employee', data={'name':'kazu'}
)
print(r.text)


r = requests.put(
    'http://127.0.0.1:5000/employee', data={
        'name':'kazu', 'new_name': 'matsu'}
)
print(r.text)

r = requests.delete(
    'http://127.0.0.1:5000/employee', data={'name':'kazu'}
)
print(r.text)