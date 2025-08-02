shoppingList1 = ["Milk","Cheese","Butter","Tomato","Banana","Apple"]
shoppingList2 = ["Orange","Cheese","Kiwi","Tomato","Banana","Butter"]
def fun1(a,b) :
    if a==b :
        return a
print(list(map(fun1,shoppingList1,shoppingList2)))
