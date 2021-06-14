class Employee:
    def __init__(self, employee_name, employee_number, hire_date, salary_raise = 4):
        self.__employee_name = employee_name
        self.__employee_number = employee_number
        self.__hire_date = hire_date
        self.__salary_raise = salary_raise
        
    def getEmployeeName(self):
        return self.__employee_name

    def getEmployeeNumber(self):
        return self.__employee_number
    
    def getHireDate(self):
        return self.__hire_date
    
    def getRaisePerc(self):
        return self.__salary_raise
    
    def setEmployeeName(self, name):
        self.__employee_name = name

    def setEmployeeNumber(self, number):
        self.__eemployee_number = number

    def setHireDate(self, date):
        self.__hire_date = date
        
    def setRaisePerc(self, raisePercent):
        self.__salary_raise = raisePercent
        

class ProductionWorker(Employee):

    def __init__(self, shift_number, payrate, employee_name, employee_number, hire_date, salary_raise = 4):
        super().__init__(employee_name, employee_number, hire_date, salary_raise)
        self.__shift_number = shift_number
        self.__payrate = payrate
        

    def getShiftNumber(self):
        return self.__shift_number
    def getPayRate(self):
        return self.__payrate
    

    def setShiftNumber(self, shift):
        self.__shift_number = shift
    def setPayRate(self, payrate):
        self.__payrate = payrate
    def setRaise(self):
        self.__payrate=self.__payrate *(1+(self.getRaisePerc()/100))
        
class ShiftSupervisor(Employee):
    def __init__(self, shift_number, payrate, employee_name, employee_number, hire_date,salary_raise = 7.5):
        super().__init__(employee_name, employee_number, hire_date, salary_raise)
        self.__shift_number = shift_number
        self.__payrate = payrate
  
    def getShiftNumber(self):
        return self.__shift_number
    
    def getPayRate(self):
        return self.__payrate
    
    def setShiftNumber(self,shift):
        self.__shift_number = shift
        
    def setPayRate(self,payrate):
        self.__payrate = payrate
        
    def setRaise(self):
        self.__payrate = self.__payrate * (1+(self.getRaisePerc()/100))
        
class Managers(Employee):
    
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

print("------------------------------------------------")
print("Production Worker")
production_worker = ProductionWorker(2, 1800, "Anne McQueen", 1234, "April 28, 2021")
print("Employee: ", production_worker.getEmployeeName())
print("Employee Number:", production_worker.getEmployeeNumber())
print("Hire Date: ", production_worker.getHireDate())
print("Shift Number: ", production_worker.getShiftNumber())
print("Salary: $", production_worker.getPayRate())
print("Raise: ", production_worker.getRaisePerc(), "%")
production_worker.setRaise()
print("Salary after raise: $", round(production_worker.getPayRate(), 2))

print("------------------------------------------------")
print("Shift Supervisor")
shift_supervisor = ShiftSupervisor(1, 3129,"David Gordon", 4567,"January 14, 2021")

print("Employee: ", shift_supervisor.getEmployeeName())
print("Employee Number:", shift_supervisor.getEmployeeNumber())
print("Hire Date: ", shift_supervisor.getHireDate())
print("Shift Number: ", shift_supervisor.getShiftNumber())
print("Salary: $", shift_supervisor.getPayRate())
print("Raise: ", shift_supervisor.getRaisePerc(), "%")
shift_supervisor.setRaise()
print("Salary after raise: $", round(shift_supervisor.getPayRate(), 2))

print("------------------------------------------------")
print("Manager")
departments = ["Production", "Sales", "Employee"]
manager = Managers(4000, departments, "Paul McDonald", 7891, "December 25, 2020")
print("Employee: ", manager.getEmployeeName())
print("Employee Number:", manager.getEmployeeNumber())
print("Departments: ", manager.getManagedDepartment())
print("Hire Date: ", manager.getHireDate())
print("Salary: $", manager.getSalaryAmount())
print("Raise: ", manager.getRaisePerc(), "%")
manager.setRaise()
print("Salary after raise: $", round(manager.getSalaryAmount(), 2))

print("------------------------------------------------")
