import requests
from bs4 import BeautifulSoup
import json

class Model:
    def __init__(self,name,price):
        self.name=name
        self.price=price


res=requests.get("https://www.entekhabcenter.com/product-category/product/audio-video/television")
print(res.status_code)

soup=BeautifulSoup(res.content,"html.parser")
# print(soup.body)

TV=soup.select("div.product")
# print(len(TV))
# tvname=TV.select_one("h3").text
# tvprice=TV.select_one("div.text-end span.new-price").contents[0]

objectlist=[]
for item in TV :
    tvname=item.select_one("h3").text
    tvprice=item.select_one("div.text-end span.new-price").contents[0]
    Model1=Model(tvname,tvprice)
    objectlist.append(Model1.__dict__)

with open("Web Scraping\Scrap4\Scrap4.json","w",encoding="utf-8") as file1 :
    json.dump(objectlist,file1,ensure_ascii=False,indent=4)