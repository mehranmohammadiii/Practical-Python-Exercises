from datetime import datetime
from json import load,dump
from jmespath import search

class My_Exception_Handling(Exception) :
    def __init__(self,message):
        super().__init__(message)
        self.__message=message
    def __str__(self):
        return 'EROR is : '+ self.__message+'...'
# ------------------------------------------------------------
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
# ------------------------------------------------------------
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
# ------------------------------------------------------------
class Customer(Base) :
    def __init__(self,customercode,name,family,mobileNumber):
        if self.__ChechCustomerCode(customercode)==False :
            raise My_Exception_Handling(" in customer az ghabl vojid darad")
        self.__customercode=customercode
        self.__name=name
        self.__family=family
        self.__mobileNumber=mobileNumber
    
    def __ChechCustomerCode(self,customercode) :
        try:
            with File("Shop/Customers.json","r") as file1 :
                objectlist=load(file1)
                cu=search("[]._Customer__customercode",objectlist)
                if customercode  in cu :
                    return False
    
        except FileNotFoundError:
            print(" file not")    
        except My_Exception_Handling as e:
            print(e)  
        except Exception as e :
            return True  
# ------------------------------------------------------------
class Product(Base) :
    def __init__(self,productCode,productName,price,productGroupName):
        self.__productCode=productCode
        self.__productName=productName
        self.__price=price
        self.__productGroupName=productGroupName
# ------------------------------------------------------------
class Bill(Base) :
    def __init__(self,billCode,customerCode):
        self.__billCode=billCode
        self.__customerCode=customerCode
        self.__billDate=str(datetime.now())
        self.__billDetails=[]
    
    def AddBillDetails(self,BillDetails) :
        self.__billDetails.append(BillDetails)
# ------------------------------------------------------------
class BillDetails() :
    def __init__(self,billDetailCode,billCode,productCode,productCount):
        self.__billDetailCode=billDetailCode
        self.__billCode=billCode
        self.__productCode=productCode
        self.__productCount=productCount
# ------------------------------------------------------------
class Shop(Base) :
    def __init__(self,name):
        self.__name=name
        self.__Customerlist=self._ReadObjectFromJsonFile("Shop/Customers.json")
        self.__Productlist=self._ReadObjectFromJsonFile("Shop/Products.json")
        self.__Billlist=self._ReadObjectFromJsonFile("Shop/Bills.json")

    def __ShowObject(self,object) :
        if len(object)>0 :
            return object

    def ShowCustomerlist(self):
        return self.__ShowObject(self.__Customerlist)

    def ShowProductlist(self):
        self.__ShowObject(self.__Productlist)
        
    def ShowBilllist(self):
        self.__ShowObject(self.__Billlist)
# ------------------------------------------------------------
try :
    c1=Customer(1,"Mehran","Mohammadi","092000000") 
    Customer.ReadAndWrite("Shop/Customers.json",c1.__dict__) 
    c2=Customer(2,"Ali","Ahmadi","092000000")
    Customer.ReadAndWrite("Shop/Customers.json",c2.__dict__) 
    c3=Customer(2,"Ali","Ahmadi","092000000")  
    Customer.ReadAndWrite("Shop/Customers.json",c3.__dict__)
except My_Exception_Handling as e :
    print(e)

p1=Product(100,"pofak",10000,"tanagholat")         
p2=Product(101,"chips",150000,"tanagholat")
p3=Product(102,"tomato",75000,"tanagholat")         
p4=Product(103,"banana",150000,"tanagholat") 


b1=Bill(1,1)                                      
bd1=BillDetails(1,1,100,5)
bd2=BillDetails(2,1,101,8)
b1.AddBillDetails(bd1.__dict__)
b1.AddBillDetails(bd2.__dict__)
   
b2=Bill(2,2)                                      
bd3=BillDetails(3,2,103,2)
bd4=BillDetails(4,2,104,6)
b2.AddBillDetails(bd3.__dict__)
b2.AddBillDetails(bd4.__dict__)

Product.ReadAndWrite("Shop/Products.json",p1.__dict__)
Product.ReadAndWrite("Shop/Products.json",p2.__dict__)
Product.ReadAndWrite("Shop/Products.json",p3.__dict__)
Product.ReadAndWrite("Shop/Products.json",p4.__dict__)

Bill.ReadAndWrite("Shop/Bills.json",b1.__dict__)
Bill.ReadAndWrite("Shop/Bills.json",b2.__dict__)

# Shop1=Shop("Shop1")
# print(Shop1.ShowCustomerlist())