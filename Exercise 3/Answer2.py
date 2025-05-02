from abc import ABC,abstractmethod
class participant(ABC):
    def __init__(self,Name,Family,NationalCode,Address,StudyField):
        self._Name=Name
        self._Family=Family
        self._NationalCode=NationalCode
        self._Address=Address
        self._StudyField=StudyField
    
    @abstractmethod
    def ScoreCalculation(self):
        pass

    def Show(self):
        return f"{self._Name}\t{self._Family}\t{self._NationalCode}\t{self._Address}\t{self._StudyField}"
# -----------------------------------------------------------------
class FreeParticipant(participant):
    def __init__(self, _Name, _Family, _NationalCode, _Address, _StudyField,InterviewScore,WrittenScore):
        super().__init__(_Name, _Family, _NationalCode, _Address, _StudyField)
        self.__InterviewScore=InterviewScore
        self.__WrittenScore=WrittenScore
    
    def ScoreCalculation(self):
        if self.__InterviewScore >100 or self.__InterviewScore<0 :
            return f"Invalid InterviewScore"
        elif self.__WrittenScore >100 or self.__WrittenScore<0 :
            return f"Invalid WrittenScore"
        else:
            return (self.__InterviewScore+self.__WrittenScore)/2
        
    def Show(self):
        return f"{participant.Show(self)}\t{self.__InterviewScore}\t{self.__WrittenScore}"
    
    @property
    def InterviewScore(self):
        return self.__InterviewScore

    @InterviewScore.setter
    def InterviewScore(self,New):
        self.__InterviewScore=New

    @property
    def WrittenScore(self):
        return self.__WrittenScore

    @WrittenScore.setter
    def WrittenScore(self,New):
        self.__WrittenScore=New
# -----------------------------------------------------------------
class EliteStudent(participant):
    def __init__(self, _Name, _Family, _NationalCode, _Address, _StudyField, Average, UniversityRank):
        super().__init__(_Name, _Family, _NationalCode, _Address, _StudyField)
        self.__Average=Average
        self.__UniversityRank=UniversityRank
    
    def ScoreCalculation(self):
        if isinstance(self.__CheckAverage(),int) and isinstance(self.__CheckRank(),int) :
            return (self.__CheckAverage()+self.__CheckRank())/2
        else :
            if isinstance(self.__CheckAverage(),str):
                return self.__CheckAverage()
            elif isinstance(self.__CheckRank(),str):
                return self.__CheckRank()

    def __CheckAverage(self):
        if self.__Average >=16 and self.__Average<=17.5 :
            return 60
        elif self.__Average>17.5 and self.__Average<=18.5 :
            return 80
        elif self.__Average>18.5 and self.__Average<=20 :
            return 100
        else :
            return f"Invalid Average"

    def __CheckRank(self):
        if self.__UniversityRank==1 :
            return 100
        elif self.__UniversityRank==2 :
            return 80
        elif self.__UniversityRank==3 :
            return 60
        else :
            return f"Invalid Rank"
    
    def Show(self):
        return f"{participant.Show(self)}\t{self.__Average}\t{self.__UniversityRank}"
    
    @property
    def Average(self):
        return self.__Average
    
    @Average.setter
    def Average(self,New):
        self.__Average=New
    
    @property
    def UniversityRank(self):
        return self.__UniversityRank
    
    @UniversityRank.setter
    def UniversityRank(self,New):
        self.__UniversityRank=New
# -----------------------------------------------------------------
class Employee(participant):
    def __init__(self, _Name, _Family, _NationalCode, _Address, _StudyField, PerformanceScore, workingYears):
        super().__init__(_Name, _Family, _NationalCode, _Address, _StudyField)
        self.__PerformanceScore=PerformanceScore
        self.__workingYears=workingYears

    def ScoreCalculation(self):
        if 1<self.__workingYears<=5 :
            return ((self.__PerformanceScore*0.1)+self.__PerformanceScore)
        else :
            return ((self.__PerformanceScore*0.2)+self.__PerformanceScore)
        
    def Show(self):
        return f"{participant.Show(self)}\t{self.__PerformanceScore}\t{self.__workingYears}"
# ----------------------------------------------------------------------------------------------------------
FreeParticipant1=FreeParticipant('Ali','Ahmadi','06455124','Tehran','IT',90,92)
FreeParticipant2=FreeParticipant('Amir','Hamidi','06455124','Tehran','IT',60,70)
FreeParticipant3=FreeParticipant('Ahmad','Akbari','06455124','Tehran','IT',50,80)

EliteStudent1=EliteStudent('Sara','Beyki','06412135','Mashhad','Web',17.60,2)
EliteStudent2=EliteStudent('Mehran','Mohammadi','06412135','Birjand','Back',18.60,2)
EliteStudent3=EliteStudent('Saeed','Sadeghi','06412135','Shiraz','Web',17.65,1)

Employee1=Employee('Ali','Amiri','065121841','Ahvaz','TB',80,4)
Employee2=Employee('Danial','Akbari','065121841','Birjand','TB',70,10)
Employee3=Employee('Morteza','Hoseini','065121841','Ahvaz','TB',90,15)

print(100*'*')
list1=[FreeParticipant1,FreeParticipant2,FreeParticipant3,
       EliteStudent1,EliteStudent2,EliteStudent3,
       Employee1,Employee2,Employee3]

for Object in list1 :
    if Object.ScoreCalculation()>=90 :
        print(Object.Show(),'\t\t','Score is : ',Object.ScoreCalculation())