city_List = ["city1","city2","city3","city4","city5","city6"]
population_List = [300000, 1000000, 3800000, 500000, 1900000, 100000]
area_List_squarekilometer = [100, 200, 500, 150, 300, 100]

def Km_To_Hectare(item) :
        return item*100

def Calculating_Population(item1,item2) :
    return int(item1/Km_To_Hectare(item2))

def Show_Population(dic) :
    for Density,city in dic.items() :
        if Density>=50 :
            print(f'{city} : {Density}')

dic1={key:value for key,value in zip([Calculating_Population(population_List[i],area_List_squarekilometer[i]) for i in range(6)],city_List)}

for Density,city in dic1.items() :
    print(f'{city} : {Density}')

print()

Show_Population(dic1)

