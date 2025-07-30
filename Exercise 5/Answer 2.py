def Firstnumbers() :
    temp=2
    yield temp
    while True :
        status=True
        temp+=1
        for i in range(2,temp) :
            if temp%i==0 :
                status=False
                break
        if status : yield temp

obj=Firstnumbers()
for i in range(100) :
    print(next(obj))