from collections import Counter
student_List1 = [{"Name":"Ali Rezaee", "Age":25},
                 {"Name":"Reza Ahmadi","Age":28},
                 {"Name":"Sara Akbari","Age":25},
                 {"Name":"Bahar Najafi","Age":23},
                 {"Name":"Iman Mohamadi","Age":25},
                 {"Name":"Sima Shaker","Age":25},
                 {"Name":"Negin Ghazi","Age":29},
                 {"Name":"Maryam Yaghoubi","Age":25},
                 {"Name":"Mitra Sharif","Age":23},
                 {"Name":"Ahmad Moradi","Age":25}]

student_List2 = [{"Name":"Amir Radi", "Age":23},
                 {"Name":"Reza Ardakani","Age":23},
                 {"Name":"Sima Sadr","Age":26},
                 {"Name":"Bahman Najafi","Age":30},
                 {"Name":"Mina Mohamadi","Age":23},
                 {"Name":"Mitra Moradi","Age":23},
                 {"Name":"Narges Arab","Age":30},
                 {"Name":"Ali Eshtiyaghi","Age":32}]
templist1=[]
templist2=[]
for item in student_List1 :
    templist1.append(item["Age"])
print(Counter(templist1).most_common(1))

for item in student_List2 :
    templist2.append(item["Age"])
print(Counter(templist2).most_common(1))