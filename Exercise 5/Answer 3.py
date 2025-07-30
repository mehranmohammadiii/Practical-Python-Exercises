def getlist(list,index) :
    for item in list :
        yield(index,item)
        index+=1

for item in getlist([1,2,5,8,15,45,7,3,19],3) :
    print(item)
# # ------------------------------------
def range_(start, stop, step) :
    while True :
        if start>=stop :
            break
        yield start
        start+=step

for i in range_(0,10,2) :
    print(i)
# # ------------------------------------
def pow(num):
    return num*num

def mymap (function, lst):
    i = 0
    while i < len(lst):
        yield function(lst[i])
        i += 1

list1=[2,4,6]
print (list (mymap (pow, list1)))
# ------------------------------------
def fun(n) :
    temp=2
    yield temp
    while True :
        if temp >n :
            break
        yield temp
        temp+=1
for i in fun(10) :
    print(i)
# ------------------------------------
def squares_up_to(num):
    n = 1
    while n ** 2 <= num:
        yield n ** 2
        n += 1
print (list (squares_up_to (20)))
# ------------------------------------