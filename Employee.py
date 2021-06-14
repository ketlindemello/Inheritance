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
