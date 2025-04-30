class Address:
    def __init__(self,CityName,StreetName,HouseNumber):
        self._CityName=CityName
        self._StreetName=StreetName
        self._HouseNumber=HouseNumber

    def _Show(self):
        return f"{self._CityName}\t{self._StreetName}\t{self._HouseNumber}"
    
    def _AddDictAddres(self):
        DictAddres={}
        DictAddres ['CityName']= self._CityName
        DictAddres ['StreetName']= self._StreetName
        DictAddres ['HouseNumber']= self._HouseNumber
        return DictAddres
# -----------------------------------------------------------
class Person:
    def __init__(self,CustomerCode,Name,Family,ContactNumber,Email):
        self._CustomerCode=CustomerCode
        self._Name=Name
        self._Family=Family
        self._ContactNumber=ContactNumber
        self._Email=Email

    def _Show(self):
        return f"{self._CustomerCode}\t{self._Name}\t{self._Family}\t{self._ContactNumber}\t{self._Email}"
    
    def _AddDictPerson(self):
        DictPerson={}
        DictPerson ['CustomerCode']= self._CustomerCode
        DictPerson ['Name']= self._Name
        DictPerson ['Family']= self._Family
        DictPerson ['ContactNumber']= self._ContactNumber
        DictPerson ['Email']= self._Email
        return DictPerson
# -----------------------------------------------------------
class Contact(Person,Address):
    def __init__(self, _CustomerCode, _Name, _Family, _ContactNumber, _Email, _CityName, _StreetName, _HouseNumber):
        Person.__init__(self,_CustomerCode, _Name, _Family, _ContactNumber, _Email)
        Address.__init__(self,_CityName,_StreetName,_HouseNumber)
        self.Dict={}

    def MergedDict(self):
        self.Dict=self._AddDictAddres() | self._AddDictPerson()
        return self.Dict
    
    def Show(self):
        return f"{Address._Show(self)}\t{Person._Show(self)}"
# -----------------------------------------------------------
class PhoneBook:
    def __init__(self):
        self.__PhoneBookList=[] 

    def AddContact(self,ContactDict):
        self.__PhoneBookList.append(ContactDict)

    def SearchCustomer(self,Family):
        self.status=0
        for object in self.__PhoneBookList :
            if object ['Family']==Family :
                self.status=1
                Contact1=Contact(object ['CustomerCode'],object['Name'],
                                 object['Family'],object['ContactNumber'],
                                 object['Email'],object['CityName'],
                                 object['StreetName'],object['HouseNumber'])
                print(Contact1.Show())

        if self.status==0 :
            print("Unknown Customer")

    def Show(self):
        for Object in self.__PhoneBookList :
            for key,value in Object.items() :
                print(key,":",value,end=" ")  
            print(127*"*")
# -----------------------------------------------------------
Contact1=Contact(1,'Mehran','Mohammadi','09208199895','123@gmail.com','Tehran','ghafari',12)
Contact2=Contact(2,'Mehdi','Ahmadi','09208194511','123@gmail.com','Tehran','ghafari',51)
Contact3=Contact(3,'Ali','Rezayi','0915819912','123@gmail.com','Mashhad','Hafez',68)
Contact4=Contact(4,'Mehran','Rezayi','0915819912','123@gmail.com','Mashhad','Hafez',85)

ContactDict1=Contact1.MergedDict()
ContactDict2=Contact2.MergedDict()
ContactDict3=Contact3.MergedDict()
ContactDict4=Contact4.MergedDict()

PhoneBook1=PhoneBook()
PhoneBook1.AddContact(ContactDict1)
PhoneBook1.AddContact(ContactDict2)
PhoneBook1.AddContact(ContactDict3)
PhoneBook1.AddContact(ContactDict4)
PhoneBook1.Show()
print()

PhoneBook1.SearchCustomer("Rezayi")
