class Person :
    def __init__(self, Name, Family):
      self._Name = self.__CapitalizeName(Name)
      self._Family = self.__CapitalizeName(Family)

    def __CapitalizeName(self,Str) :
        return Str.upper()
    
    def _ShowInformation(self) :
        return f"Nami is : {self._Name}\tFmamily is : {self._Family}"
# --------------------------------------------------------------------------   
class Manager(Person) :
    ManagerCount=0
    def __init__(self ,Name, Family, PersonnelCode, SalaryAmount):
        Person.__init__(self,Name,Family)
        self.__PersonnelCode=PersonnelCode
        self.__SalaryAmount=SalaryAmount
        Manager.ManagerCount+=1

    def SetSalaryAmount(self,NewSalary) :
        self.__SalaryAmount=NewSalary
    
    def GetSalaryAmount(self) : 
        return self.__SalaryAmount
    
    def ShowManagerInformation(self) :
        return f"{self._ShowInformation()}\tPersonnelCode is :{self.__PersonnelCode}\tSalaryAmount is :{self.__SalaryAmount}"
# --------------------------------------------------------------------------    
class Employee(Person) :
    employeeCount=0
    def __init__(self,Name,Family,PersonnelCode,Rank):
        Person.__init__(self,Name,Family)
        self.__PersonnelCode=PersonnelCode
        self.__Rank=self.CheckRank(Rank)
        Employee.employeeCount+=1

    def CheckRank(self,Rank) :
        if Rank.upper() not in ["A","B","C","D"] :
            return "NULL"
        else :
            return Rank
        
    def SetRank(self,NewRank) :
        self.__Rank=NewRank
    
    def GetRank(self) :
        return self.__Rank

    def ShowEmployeeInformation(self) :
        return f"{self._ShowInformation()}\tPersonnelCode is : {self.__PersonnelCode}\tRank is : {self.__Rank}"
# ----------------------------------------------------------------------------   
class Intern(Person) :
    InternCount=0
    def __init__(self, Name, Family):
        Person.__init__(self,Name,Family)
        self.__InternshiPduration=12
        Intern.InternCount+=1
    
    def ShowInternInformation(self) :
        return f"{self._ShowInformation()}\tInternshiPduration is : {self.__InternshiPduration}"
# ---------------------------------------------------------------------------- 
manager_List = []

manager1 = Manager("reza","Ahmadi",11,20000000)
manager2 = Manager("sara","Biniaz",12,25000000)
manager3 = Manager("ali","Ganji",13,18000000)
manager_List.append(manager1)
manager_List.append(manager2)
manager_List.append(manager3)

print("List of Managers:\n")
i = 1
for manager in manager_List:
    print(i,".",manager.ShowManagerInformation())
    i += 1
print()
print("Number of Managers:",Manager.ManagerCount)
print()

manager1.SetSalaryAmount(1300000)
print(manager1.GetSalaryAmount())
# -----------------

employee_List = []

employee1 = Employee("Maryam","rezaee",1,"A")
employee2 = Employee("Milad","Karami",3,"A")
employee3 = Employee("Ahmad","shahed",5,"C")
employee4 = Employee("Zahra","Asadi",2,"B")
employee_List.append(employee1)
employee_List.append(employee2)
employee_List.append(employee3)
employee_List.append(employee4)
print()

print("List of Employees:\n")

for employee in employee_List:
    print(employee.ShowEmployeeInformation())

print()
print("Number of Employees:",Employee.employeeCount)
print()

employee3.SetRank("D")
print(employee3.GetRank())
print()
# -----------------
intern_List = []

intern1 = Intern("sima","rahmani")
intern2 = Intern("mohammad","majd")
intern_List.append(intern1)
intern_List.append(intern2)

print("List of Interns:\n")
for intern in intern_List:
    print(intern.ShowInternInformation())

print()
print("Number of Interns:",Intern.InternCount)
print()