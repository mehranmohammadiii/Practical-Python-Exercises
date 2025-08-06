import requests
from bs4 import BeautifulSoup
import re
import itertools
import json

class Model:
    def __init__(self,name,date,loction):
        self.name=name
        self.date=date
        self.loction=loction

res=requests.get("https://conferenceindex.org/conferences/programming-languages")
print(res.status_code)
soup1=BeautifulSoup(res.content,"html.parser")

# title=soup1.select_one("h1").text
# print(title)                                #1
# print(100*'-')

list_month=soup1.select("div.card-body")[0]
list_li=list_month.select("ul > li")

# for item in list_li :
#     print(item.text.strip())                #2
# print(100*'-')

# list_li=list_month.select("ul > li")
# for item in list_li :
#     print(re.findall("[A-Z,Aa-z]{3}\s{1}\d{2}",item.text.strip()))      #3
# print(100*'-')

# list_li=list_month.select("ul > li")
# for item in list_li :
#     print(item.a['href'])                                               #4
# print(100*'-')

# list_li=list_month.select("ul > li")
# for item in list_li :
#     print(item.a.text.strip())                                          #5
# print(100*'-')

# regx1=re.compile(".*Computing.*")
# list1=[item.a.text.strip() for item in list_li]
# print(list(filter(regx1.match,list1)))                                  #6
# print(100*'-')

listname=[]
for item in list_li :
    listname.append(item.a.text.strip())                                  # list name
# print(listname)

nestedlist_date=[re.findall("[A-Z,Aa-z]{3}\s{1}\d{2}",item.text.strip()) for item in list_li]   #list date
listdate=list(itertools.chain.from_iterable(nestedlist_date))
# print(listdate)

nestedlist_loction=[re.findall(".*-(.*)",item.text.strip()) for item in list_li]   #list loction
listloction=list(itertools.chain.from_iterable(nestedlist_loction))
# print(listloction)

templist=[]
for i in range(len(listname)) :
    Model1=Model(listname[i],listdate[i],listloction[i])
    templist.append(Model1.__dict__)

with open("Web Scraping\Scrap2\Scrap2.json","w") as file1 :
    json.dump(templist,file1,indent=4)


