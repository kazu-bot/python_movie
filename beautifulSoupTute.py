#BeautifulSoupでWEBスクレイピングを行う。

from bs4 import BeautifulSoup
import requests

#python公式のタグや文字を取得する
html = requests.get('https://www.python.org')

soup = BeautifulSoup(html.text, 'lxml')

title = soup.find_all('title')
print(title[0].text)

intro = soup.find_all('div',{'class':'introduction'})
print(intro[0].text)