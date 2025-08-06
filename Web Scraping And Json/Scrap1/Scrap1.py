import re
import requests
from bs4 import BeautifulSoup
import json

class Modle:
    def __init__(self,name,price,description,img,reviews,starsnumber):
        self.name=name
        self.price=price
        self.description=description
        self.img=img
        self.reviews=reviews
        self.starsnumber=starsnumber
    
    def __str__(self):
        return f"{self.name}\t{self.price}\t{self.description}\t{self.reviews}\t{self.starsnumber}\t{self.img}"
# ----------------------------------------------------------------------------------------------------
res=requests.get("https://webscraper.io/test-sites/e-commerce/static")
print(res.status_code)
soup=BeautifulSoup(res.content,"html.parser")
list1=soup.select("div.card.thumbnail")

# print(len(list1))
# print(list1)
# print(100*'-')
# print(list1[0].div)


# print(list1[1].select("a.title")[0].text.strip())                                         #title
# print(list1[1].select("div.caption > h4:nth-of-type(2) > a.title")[0].text.strip())       #title
# print(list1[1].select("div.caption > h4 > span")[0].text.strip())                         #price
# print(list1[1].select("span")[0].text.strip())                                            #price
# print(list1[1].select("p")[0].text.strip())                                               #description
# print(list1[1].select("div.caption > p.description.card-text")[0].text.strip())           #description
# print(list1[1].select("img")[0]["src"])                                                   #img
# print(list1[1].select("div.product-wrapper.card-body > img.img-fluid")[0]["src"])         #img
# print(list1[1].select("p.review-count > span")[0].text.strip())                           #reviews
# print(list1[1].select("div.ratings > p.review-count > span")[0].text.strip())             #reviews
# starsnumber=list1[1].select("div.ratings > p:nth-of-type(2) span.ws-icon")                #starsnumber
# print(len(starsnumber))

objectlist=[]
for item in  list1 :
    title=item.select("div.caption > h4:nth-of-type(2) > a.title")[0].text.strip()

    price=item.select("div.caption > h4 > span")[0].text.strip()

    description=item.select("div.caption > p.description.card-text")[0].text.strip()

    img=item.select("div.product-wrapper.card-body > img.img-fluid")[0]["src"]

    reviews=item.select("div.ratings > p.review-count > span")[0].text.strip()

    starsnumber=len(item.select("div.ratings > p:nth-of-type(2) span.ws-icon"))
    
    Modle1=Modle(title,price,description,img,reviews,starsnumber)
    objectlist.append(Modle1.__dict__)
with open("Web Scraping\Scrap1\Scrap1.json","w") as file1 :
    json.dump(objectlist,file1,indent=4)