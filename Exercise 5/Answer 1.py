def factorial_iterative():
    result = 1
    t=1
    yield result
    while True :
        t+=1
        result*=t
        yield result




obj=factorial_iterative()
for i in range(10):
    print(next(obj))






