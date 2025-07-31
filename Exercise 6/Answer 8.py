import collections
# --------------------------------------------------------------------
class MyString(collections.UserString):
    def reverse(self):
        tempStr = ""
        for i in range(len(self.data)-1,-1,-1):
            tempStr+=self.data[i]
        return tempStr
str1 = MyString("hello")
print(str1.reverse())
# ======================================================================
class MyString(collections.UserString):
    def insert(self,word1,word2):
        index = self.data.find(word1)
        return self.data[:index]+word2+" "+self.data[index:]
str1 = "Python is an open source language."
mystring = MyString(str1)
print(mystring.insert("language","programming"))