from abc import ABC
class ProgrammingLanguageCourse(ABC):
    def __init__(self,StartDate,EndDate,CourseLevel,CourseTeacher):
        self._StartDate=StartDate
        self._EndDate=EndDate
        self._CourseLevel=CourseLevel
        self._CourseTeacher=CourseTeacher
        self._DayList=[]
      
    def AddDay(self,Day):
        return self._DayList.append(Day)
    
    def _Show(self):
        return f"{self._StartDate}\t{self._EndDate}\t{self._CourseLevel}\t{self._CourseTeacher}"
#--------------------------------------------------------
class Python(ProgrammingLanguageCourse):
    def __init__(self, StartDate, EndDate, CourseLevel, CourseTeacher, CourseCode, CourseFee):
        super().__init__(StartDate, EndDate, CourseLevel, CourseTeacher)
        self.__CourseCode=CourseCode
        self.__CourseFee=CourseFee

    def ShowPython(self):
        return f"Python : {self.__CourseCode}\t{self._Show()}\t{self.__CourseFee}\n{self._DayList}"
        
#--------------------------------------------------------
class Java(ProgrammingLanguageCourse):
    def __init__(self, StartDate, EndDate, CourseLevel, CourseTeacher, CourseCode, CourseFee):
        super().__init__(StartDate, EndDate, CourseLevel, CourseTeacher)
        self.__CourseCode=CourseCode
        self.__CourseFee=CourseFee
      
    def ShowJava(self):
        return f"Java : {self.__CourseCode}\t{self._Show()}\t{self.__CourseFee}\n{self._DayList}"
#--------------------------------------------------------
class PHP(ProgrammingLanguageCourse):
    def __init__(self, StartDate, EndDate, CourseLevel, CourseTeacher, CourseCode, CourseFee):
        super().__init__(StartDate, EndDate, CourseLevel, CourseTeacher)
        self.__CourseCode=CourseCode
        self.__CourseFee=CourseFee

    def ShowPHP(self):
        return f"PHP : {self.__CourseCode}\t{self._Show()}\t{self.__CourseFee}\n{self._DayList}"
#--------------------------------------------------------
P1=Python('1403/05/01','1403/10/30','Basic Level','Mr Ahmadi',10,3500000)  
P2=Python('1404/05/01','1404/10/30','Advanced Level','Mr Ahmadi',11,5000000)
P1.AddDay('Sunday')
P1.AddDay('Tuesday')
P2.AddDay('Saturday')
P2.AddDay('Wednesday')
print(P1.ShowPython())
print(P2.ShowPython())
J1=Java('1403/01/01','1403/05/30','Basic Level','Mr Mohammadi',20,3000000)
J2=Java('1404/01/01','1404/01/30','Advanced Level','Mr Mohammadi',21,4500000)
J1.AddDay('Thursday')
J2.AddDay('Tuesday')
print(J1.ShowJava())
print(J2.ShowJava())
PH1=PHP('1403/01/01','1403/05/30','Basic Level','Mr Hasani',30,4000000)
PH2=PHP('1404/01/01','1404/01/30','Advanced Level','Mr Hasani',31,5500000)  
PH1.AddDay('Wednesday')
PH1.AddDay('Saturday')
PH2.AddDay('Tuesday')
PH2.AddDay('Sunday') 
print(PH1.ShowPHP())  
print(PH2.ShowPHP())  
