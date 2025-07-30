class mylist :
    i=0
    temp=0
    def __init__(self,ob) :
       self.list1=ob

    def __iter__(self):
      return self
    
    def __next__(self):
        if self.list1==[] :
           raise RuntimeError("RuntimeError('Error:The list must not be empty...')")
        try :
            if type(self.list1[mylist.i])==int or type(self.list1[mylist.i])==float:
                mylist.temp=self.list1[mylist.i]+mylist.temp
                mylist.i+=1
                return mylist.temp
        
            else :
                mylist.temp=len(self.list1[mylist.i])+mylist.temp
                mylist.i+=1
                return mylist.temp
        except :
           mylist.temp=0
           mylist.i=0
           raise StopIteration

mylist1=mylist([])
mylist2=mylist([1,5,'abc',2.5])
mylist3=mylist(['amin',36,32.5,{25,'g','y'},'akbari'])
try :
   for i in mylist1 :
      print(i)
except RuntimeError as eror :
    print(eror)
# #----------------------------------------------------
try :
   for i in mylist2 :
      print(i,end="\t")
except RuntimeError as eror :
    print(eror)
print()
#----------------------------------------------------
try :
   for i in mylist3 :
      print(i,end="\t")
except RuntimeError as eror :
    print(eror)