class Company :
    def __init__(self, CompanyName, ManagerName, Address, EmployeesNumber, IncomeAmount ):
      self.CompanyName = CompanyName
      self.ManagerName = ManagerName 
      self.Address=Address
      self.EmployeesNumber = EmployeesNumber
      self.IncomeAmount=IncomeAmount

    def Productivity(self) :
       return (self.IncomeAmount/self.EmployeesNumber)
    
    def __str__(self):
       return f"Company Profile \n{self.CompanyName}\n{self.ManagerName}\n{self.Address}\n{self.EmployeesNumber}\n{self.IncomeAmount}"
    
C1=Company("XYZ","XXX","YYY",200,100000000)
print(C1)
print(C1.Productivity())