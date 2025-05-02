class Student :

    __SchoolName='Shahid Beheshti'
    def __init__(self,StudentCode,Name,Family,Grade):
        self.__StudentCode=StudentCode
        self.__Name=Name
        self.__Family=Family
        self.__Grade=Grade

    def __str__(self):
        return f"{self.__StudentCode}\t{self.__Name}\t{self.__Family}\t{self.__Grade}\n"
    
    def __hash__(self):
        return self.__StudentCode
    
    def __eq__(self, Object2):
        return (self.__StudentCode==Object2.__StudentCode
                and self.__Name==Object2.__Name
                and self.__Family==Object2.__Family
                and self.__Grade==Object2.__Grade)

    @classmethod
    def ChangeSchoolName(cls,NewName):
        cls.__SchoolName=NewName

    @staticmethod
    def ShowLesson(Grade):
        if Grade==1:
            return f"Grade 1 : Riyazi \t Farsi \t Ghoran \n"
        elif Grade==2:
            return f"Grade 2 : Riyazi \t Farsi \t Ghoran \t Parvarshi \n"
        elif Grade==3:
            return f"Grade 3 : Riyazi \t Farsi \t Ghoran \t Parvarshi \n"
        elif Grade==4:
            return f"Grade 4 : Riyazi \t Farsi \t Ghoran  \t Parvarshi \t Varzesh \n"
        elif Grade==5:
            return f"Grade 5 : Riyazi \t Farsi \t Ghoran \t Parvarshi \t Varzesh \n"
        elif Grade==6:
            return f"Grade 6 : Riyazi \t Farsi \t Ghoran \t Parvarshi \t Varzesh \t FoghBarname \n"
    
    @property
    def SchoolName(self):
        return self.__SchoolName

    @property
    def Grade(self):
        return self.__Grade
    
    @Grade.setter
    def Grade(self,NewGrade):
        self.__Grade=NewGrade
# ----------------------------------------------------------------------------------------------------
Student1=Student(1,'Ali','Ahmadi',4,)  
Student2=Student(2,'Mehran','Mohammadi',1)  
Student3=Student(3,'Amir','Akbari',2)  
Student4=Student(4,'Ali','Hamidi',6)  
Student5=Student(5,'Hasan','Rezayi',5)  
Student6=Student(6,'Emad','Hoseiny',3)  
Student7=Student(7,'Dainal','Jalaly',3)  
Student8=Student(8,'Mortza','Ahmadi',4,)  
Student9=Student(9,'Hamid','Arefi',6)  
Student10=Student(10,'AliReza','Ahmadi',1) 
 
print(Student.ShowLesson(3))

print()

Set1={Student1,Student2,Student3,Student4,Student5,Student6,Student7,Student8,Student9,Student10}
print(len(Set1))

print()

for Student in Set1 :
    print(Student)

print()

print(Student.SchoolName)
Student.ChangeSchoolName('Shahed')
print(Student.SchoolName)

print()

print(Student1.Grade)
Student1.Grade=5
print(Student1.Grade)

print()

print(Student1==Student2)