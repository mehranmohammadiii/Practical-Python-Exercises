from datetime import datetime,date
import khayyam

def convert() :
    date1=input(" Enter Date (For Example: 1399-06-20): ")

    datelist=[int(item) for item in date1.split("-")]
    # date2=datetime.strptime(date1,"%Y-%m-%d")
    # khayyam.jalali_date(date2.year,date2.month,date2.day)

    jalalydate=khayyam.JalaliDate(datelist[0],datelist[1],datelist[2])
    yield jalalydate.todate()
    yield abs(jalalydate.todate()-date.today()).total_seconds()/60/60/24

for item in convert() :
    print(item)
