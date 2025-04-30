
## store 1
product_Price_List1 = [5000,10000,15000,6000,25000,12000,14000,10000,7000,20000]
## store 2
product_Price_List2 = [4000,12000,16000,5000,22000,10000,16000,11000,5000,18000]
# -------------------------------------------------------------------------------------
class Product_Price:
    def __init__(self, product_Price_List):
      self.product_Price_List = product_Price_List
    
    def __add__(self,obj2):
        tempList = []
        for i in range(0,len(self.product_Price_List)):
            sum_Price = self.product_Price_List[i] + obj2.product_Price_List[i]
            tempList.append(sum_Price)
        return tempList

    # true division
    def __truediv__(self,number):
        tempList = []
        for i in range(0,len(self.product_Price_List)):
            avg_Price = self.product_Price_List[i]/number
            tempList.append(avg_Price)
        return tempList
        
    def __mul__(self,number):
        tempList = []
        for i in range(0,len(self.product_Price_List)):
            discount = number *(self.product_Price_List[i])
            tempList.append(discount)
        return tempList
        
    def __sub__(self,obj2):
        tempList = []
        for i in range(0,len(self.product_Price_List)):
            discount_Price = self.product_Price_List[i] - obj2.product_Price_List[i]
            tempList.append(discount_Price)
        return tempList
    
    # less-than operator
    def __lt__(self,obj2):
        tempList = []
        for i in range(0,len(self.product_Price_List)):
            tempList.append(self.product_Price_List[i] < obj2.product_Price_List[i])
        return tempList
# ------------------------------------------------------------------------------------------
# calculation of average prices

product1 = Product_Price(product_Price_List1)       
product2 = Product_Price(product_Price_List2) 

sum_Price_List = product1 + product2

product3 = Product_Price(sum_Price_List)

print(120*"*")
print("The average prices:")
print(product3/2) 
print(120*"*")
#---------------------------------------------------------------------
# calculation of average prices (with a discount pricing strategy)

discount_List1 = product1*0.20
discount_List2 = product2*0.20

product4 = Product_Price(discount_List1)
product5 = Product_Price(discount_List2)

discount_Price_List1 = product1 - product4
discount_Price_List2 = product2 - product5

product6 = Product_Price(discount_Price_List1)
product7 = Product_Price(discount_Price_List2)

sum_Discount_Price_List = product6 + product7

product8 = Product_Price(sum_Discount_Price_List)

print("The average prices with a discount pricing strategy:")
print(product8/2)
print(120*"*")
#---------------------------------------------------------
# comparison of two price lists

price_Comparison_List = product1<product2

for item in price_Comparison_List:
    tempList = []
    if item == True:
        tempList.append(item)
if len(tempList) > 5:
    print("The store 1 offers the customer more goods for less money")
elif len(tempList) == 5:
    print("No Difference")
else:
    print("The store 2 offers the customer more goods for less money")
    
print(120*"*")



