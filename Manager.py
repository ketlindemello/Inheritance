from Employee import Employee
class Manager(Employee):
    
    def __init__(self,salary_amount, managed_depts, employee_name, employee_number, hire_date, salary_raise = 10):
        super().__init__( employee_name, employee_number, hire_date, salary_raise)
        self.__salary_amount = salary_amount
        self.__managed_depts = managed_depts
  
    def getSalaryAmount(self):
        return self.__salary_amount
    
    def getManagedDepartment(self):
        return self.__managed_depts
    
    def setSalaryAmount(self, salary_amount):
        self.__salary_amount = salary_amount
        
    def setManagedDepartment(self, managed_depts):
        self.__managed_depts = managed_depts
        
    def setRaise(self):
        self.__salary_amount = self.__salary_amount * (1+(self.getRaisePerc()/100))
