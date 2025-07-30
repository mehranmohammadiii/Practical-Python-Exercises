class Counter :
    def __init__(self,start,end):
        self.start=start
        self.end=end

    def __iter__(self):
        return self
    
    def __next__(self) :
        self.start+=3
        if self.start>self.end :
            raise StopIteration
        return self.start

          
Counter1=Counter(10,100)
for i in Counter1 :
    print(i)