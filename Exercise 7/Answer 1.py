from datetime import datetime,date
from khayyam import JalaliDate

def check_Birth_Date(*args) :
    name_=args[0]
    family_=args[1]
    birthdate_=args[2]
    date1=datetime.strptime(birthdate_,"%Y-%m-%d")
    datejalaly=JalaliDate(date1.year,date1.month,date1.day)
    date1miladi=datejalaly.todate()

    date2=JalaliDate(1340,12,29)
    date2miladi=date2.todate()

    print(date1miladi)
    print(date2miladi)
    if date1miladi<date2miladi :
        temp=[name_,family_,date1miladi]
        Show(*temp)
    else :
        print("shoma nemitavanid vacsan beznid.....")

def Show(a,b,c) :
    print("shoma mitavanid vacsan beznid.....")
    print(f'{a}\t{b}\t{c}\t')

Name=input("Name is : ")
Family=input("Family is : ")
Birthdate=input("Birth Date is (1358-05-26) : ")  
templist=[Name,Family,Birthdate]
check_Birth_Date()