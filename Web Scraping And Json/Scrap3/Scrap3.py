import requests
from bs4 import BeautifulSoup
import json

class Model:
    def __init__(self,name,memory,selfiecamera,Rearcamera,Batterycapacity,score,discountpercent,previousprice,Newprice):
        self.name=name
        self.memory=memory
        self.selfiecamera=selfiecamera
        self.Rearcamera=Rearcamera
        self.Batterycapacity=Batterycapacity
        self.score=score
        self.discountpercent=discountpercent
        self.previousprice=previousprice
        self.Newprice=Newprice

    def __str__(self):
        return f"{self.memory}\t{self.selfiecamera}\t{self.Rearcamera}\t{self.Batterycapacity}\t{self.score}\t{self.discountpercent}\t{self.previousprice}\t{self.Newprice}"

res=requests.get("https://www.technolife.com/product/list/69_800_801/%D8%AA%D9%85%D8%A7%D9%85%DB%8C-%DA%AF%D9%88%D8%B4%DB%8C%E2%80%8C%D9%87%D8%A7")
print(res.status_code)

soup=BeautifulSoup(res.content,"html.parser")
content=soup.select("section.relative.w-full")

objectlist=[]
for item in content :
    try :
        memory=item.select("div.h-12 p")[0].text
    except :
        memory=None
    try :
        selfiecamera=item.select("div.h-12 p")[1].text
    except :
        selfiecamera=None
    try : 
        Rearcamera=item.select("div.h-12 p")[2].text
    except :
        Rearcamera=None
    
    try :  
        Batterycapacity=item.select("div.h-12 p")[3].text
    except :
        Batterycapacity=None
    try :
        mobilename=item.select_one("h2").text
    except :
        mobilename=None

    try :
        score=item.select_one("p.text-sm").text
    except :
        score=None

    try :
        discountpercent=item.select_one("span.flex").text
    except :
        discountpercent=None

    try :
        previousprice=item.select_one("div.items-end div.flex p").text
    except : 
        previousprice=None

    try :    
        # Newprice=item.select_one("div.items-end p").contents[0]
        Newprice=item.select_one("div.pt-6 div.flex p.leading-5").contents[0]
    except :
        Newprice=None
        
    Model1=Model(mobilename,memory,selfiecamera,Rearcamera,Batterycapacity,score,discountpercent,previousprice,Newprice)
    objectlist.append(Model1.__dict__)

# json
with open("Web Scraping\Scrap3\Scrap3.json","w",encoding="utf-8") as file1 :
    json.dump(objectlist,file1,ensure_ascii=False,indent=4)



