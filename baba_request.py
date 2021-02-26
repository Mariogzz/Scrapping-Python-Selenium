import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText=riot+gear")
soup = BeautifulSoup(r.text)

items = soup.select("h4")

for i in items:
    print(i.text)