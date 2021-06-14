from Employee import Employee

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
