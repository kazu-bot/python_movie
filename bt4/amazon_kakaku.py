import requests
from bs4 import BeautifulSoup

#任意のURL
URL="https://www.amazon.co.jp/Apple-%E3%82%A2%E3%83%83%E3%83%97%E3%83%AB-MWP22J-A-AirPods/dp/B07ZPS4FSW?ref_=ast_sto_dp"
#chromeに「my user agent」で分かる
HEADERS={"User-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}

def getPrice():
    page = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id = "productTitle").get_text().strip()
    price = soup.find(id="priceblock_ourprice").get_text().strip()
    print(URL)
    print(title)
    print(price)

if __name__ == '__main__':
    getPrice()
