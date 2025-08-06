import enum
from datetime import datetime
from abc import ABC,abstractmethod
from json import load,dump
from jmespath import search

class TextStatus(enum.Enum):
    unselected=1
    selected=2
    Translated=3
# -------------------------------------------------------------------------------------------------
class File() :
    def __init__(self,path,moode):
        self.__path=path
        self.__moode=moode
        self.__object=None

    def __enter__(self) :
        self.__object=open(self.__path,self.__moode)
        return self.__object
    
    def __exit__(self,*exc) :
        if self.__object :
            self.__object.close()
# -------------------------------------------------------------------------------------------------
class Base() :
    @staticmethod    
    def _ReadObjectFromJsonFile(path) :
        try:
            with File(path,"r") as file1 :
                objectlist=load(file1)
                return objectlist
        except :
            objectlist=[]
        return objectlist
    
    @staticmethod
    def _WritObjectToJsonFile(path,object) :
        with File(path,"w") as file1 :
            dump(object,file1,indent=4)

    @classmethod
    def ReadAndWrite(cls,path,object):
        readJson=cls._ReadObjectFromJsonFile(path)
        readJson.append(object)
        cls._WritObjectToJsonFile(path,readJson)
# -------------------------------------------------------------------------------------------------
class Text(ABC):
    def __init__(self,code,Language,NumberOfDays):
        self.__Status=str(TextStatus.unselected)
        self.__code=code
        self.__Language=Language
        self.__NumberOfDays=NumberOfDays
        self.__RegisterDate=str(datetime.now())
    
    def _ChangeStatus(self,NewStatus):
        self.__Status=NewStatus

    @abstractmethod
    def _GetPrice(self):
        pass

    def GetCode(self) :
        return self.__code

    def _GetStatus(self):
        return self.__Status

    def __str__(self):
        return f"{self.__code}\t{self.__Status}\t{self.__Language}\t{self.__NumberOfDays}\t{self.__RegisterDate}"
# --------------------------------------------------------------------------------------------------
class PlainText(Text,Base):
    def __init__(self,code,Language, NumberOfDays,NormalWordCount,LongWordCount):
        super().__init__(code,Language, NumberOfDays)
        self.__NormalWordCount=NormalWordCount
        self.__LongWordCount=LongWordCount
        self._Name='PlainText'
    
    def _GetPrice(self):
        return self.__NormalWordCount*500+self.__LongWordCount*600
    
    def __str__(self):
        return f"{self.__NormalWordCount}\t{self.__LongWordCount}"
# ----------------------------------------------------------------------------------------------------
class ScientText(Text,Base):
    def __init__(self,code, Language, NumberOfDays,NumberScienWords,GeneralWordCount):
        super().__init__(code,Language, NumberOfDays)
        self.__NumberScienWords=NumberScienWords
        self.__GeneralWordCount=GeneralWordCount
        self._Name='ScientText'

    def _GetPrice(self):
        return self.__GeneralWordCount*600+self.__NumberScienWords*1000

    def __str__(self):
        return f"{self.__NumberScienWords}\t{self.__GeneralWordCount}"
# -------------------------------------------------------------------------------------------------------
class HumorousText(Text,Base):
    def __init__(self,code, Language, NumberOfDays,NumberOfPhotos):
        super().__init__(code,Language, NumberOfDays)
        self.__NumberOfPhotos=NumberOfPhotos
        self._Name='HumorousText'

    def _GetPrice(self):
        return self.__NumberOfPhotos*300000

    def __str__(self):
        return f"{self.__NumberOfPhotos}"
# ------------------------------------------------------------------------------------------------------
class Motarjem(Base) :
    def __init__(self,Code,Name,Family,Phone):
        self.__IsActiv=False
        self.__Code=Code
        self.__Name=Name
        self.__Family=Family
        self.__Phone=Phone
        self.__LanguagesList=[]

    def AddLanguagesList(self,Language):
        self.__LanguagesList.append(Language)

    def SelectText(self,Texts):
        if self.__IsActiv==False :
            for text in Texts.GetTextList() :
                if text._GetStatus()==str(TextStatus.unselected) :

                    readjson=Motarjem._ReadObjectFromJsonFile("Motarjems.json")
                    for item in readjson :
                        if item['_Motarjem__Code']==self.__Code :
                            item['_Motarjem__IsActiv']=True
                    Motarjem._WritObjectToJsonFile("Motarjems.json",readjson)    

                    self.__IsActiv=True
                    text._ChangeStatus(str(TextStatus.selected))

                    print(text._Name,'\t','entekhab shod ...')
                else :
                    print(text._Name,'\t',"in matn ghablan entkhab shode.... ")
        else :
            print("shoma nmitavanid az yek order bishtar entkhab konid....")
    
    def TextDelivery(self,Texts):
        for text in Texts.GetTextList() :
            text._ChangeStatus(TextStatus.Translated)
        
        readjson=Motarjem._ReadObjectFromJsonFile("Motarjems.json")
        for item in readjson :
            if item['_Motarjem__Code']==self.__Code :
                item['_Motarjem__IsActiv']=False
        Motarjem._WritObjectToJsonFile("Motarjems.json",readjson)

        self.__IsActiv=False
    
    def __str__(self):
        temp=str(self.__IsActiv)+'\t'+str(self.__Code)+'\t'+self.__Name+'\t'+self.__Family+'\t'+self.__Phone+'\n'
        for lang in self.__LanguagesList:
            temp+=lang+'\t'
        return temp
# ------------------------------------------------------------------------------------------------------
class Order(Base):
    def __init__(self,code,motarjemcode):
        self.__code=code
        self.__motarjemcode=motarjemcode
        self.__TextList=[]
        self.__codeList=[]
   
    def to_dict(self) :
        return {
            "Code" :self.__code,
            "Motarjem Code" : self.__motarjemcode,
            "Text Code" : self.__codeList
        }

    def AddTextList(self,Text):
        self.__TextList.append(Text)
        self.__codeList.append(Text.GetCode())


    def setcode(self,code) :
        self.codelist.append(code)

    def GetPrice(self):
        sum=0
        for text in self.__TextList:
            sum+=text._GetPrice()
        return sum
    
    def GetTextList(self):
        return self.__TextList
# -----------------------------------------------------------------------------------------------------
Text1=PlainText(1,'EN',10,80,50) #40000 #30000 #70000
Text2=ScientText(2,'EN',8,30,60) #30000 #36000 #66000
Text3=PlainText(3,'EN',5,40,20) #20000 #12000 #32000
# PlainText.ReadAndWrite("Texts.json",Text1.__dict__)
# ScientText.ReadAndWrite("Texts.json",Text2.__dict__)
# PlainText.ReadAndWrite("Texts.json",Text3.__dict__)

Motarjem1=Motarjem(1,'Ali','Ahamdi','0915121211')
Motarjem2=Motarjem(2,'Mehran','Mohammadi','0915121211')
Motarjem1.AddLanguagesList('EN')
Motarjem1.AddLanguagesList('UA')
Motarjem2.AddLanguagesList('EN')
# Motarjem.ReadAndWrite("Motarjems.json",Motarjem1.__dict__)
# Motarjem.ReadAndWrite("Motarjems.json",Motarjem2.__dict__)

Order1=Order(1,1)
Order1.AddTextList(Text1)
# Order1.AddTextList(Text2)
# Order1.AddTextList(Text3)
Motarjem1.SelectText(Order1)
# Order.ReadAndWrite("orders.json",Order1.to_dict())
# Motarjem1.TextDelivery(Order1)


# print(Order1.GetPrice())
# print(Text1._GetStatus())
# print(Motarjem1)
# Motarjem1.SelectText(Order1)
# print(Text1._GetStatus())
# print(Motarjem1)

# Text4=PlainText(4,'EN',4,40,50)
# Order2=Order(2,2)
# Order2.AddTextList(Text4)


# Motarjem1.SelectText(Order2)

# Motarjem1.SelectText(Order2)

# Motarjem2.SelectText(Order1)