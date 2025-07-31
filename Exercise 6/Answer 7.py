import collections
Mobile = collections.namedtuple("Mobile","Brand Model Price Colors")
m1 = Mobile("Samsung","xxx", 6000000,["red","black"])
m2 = Mobile("Apple","xxx", 20000000,["blue","black","red"])
m3 = Mobile("Nokia","xxx", 8000000,["red","black","white","pink"])
m4 = Mobile("Samsung","xxx", 12000000,["red","white"])
mobile_List = []
for mobile in (m1,m2,m3,m4):
    mobile_List. append(mobile._asdict())
for mobile in mobile_List:
    print(mobile)