from itertools import chain,compress,combinations
from operator import itemgetter
expert_List1 = [("Ali","Ahmadi","M",35), ("Sima","Sadri","C",39),
("Ahmad","Moradi","M",30), ("Ftemeh","Majd","C",29), ("Sara","Biglar","IE",27),
("Reza","Rahnama","EE",45)]

expert_List2 = [("Mina","Gohari","EE",40), ("Iman","Shams","M",26),
("Farzad","Yeganeh","M",41), ("Ali","Imani","C",33), ("Aref","Alameh","M",32),
("Narges","Sohrabi","C",35)]

chain1=list(chain.from_iterable([expert_List1,expert_List2]))
print(sorted(chain1,key=itemgetter(2)))
print()
name_M=list(compress(sorted(chain1,key=itemgetter(2)),[0,0,0,0,0,0,0,1,1,1,1,1]))
print(name_M)
print()
print(list(combinations(name_M,3)))