import math
number_List = [4, 3, 8, 0, -3, -45, 2, 10, -16, 23, 9, 1, -6, 55, 3.4, 6, 11.5]


def mainfun(fun) :
    def inner(list1) :
        numberList1=[]
        for item in list1 :
            if item > 0 :
                numberList1.append(item)
        return fun(numberList1)
    return inner

@mainfun
def fact(list) :
    temp=[]
    for item in list :
        temp.append(math.factorial(int(item)))
    return temp    

print(fact(number_List))
