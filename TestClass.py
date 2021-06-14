
from ShiftSupervisor import ShiftSupervisor
from ProductionWorker import ProductionWorker
from Manager import Manager
from Employee import Employee

def main():
    
    
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
    manager = Manager(4000, departments, "Paul McDonald", 7891, "December 25, 2020")
    print("Employee: ", manager.getEmployeeName())
    print("Employee Number:", manager.getEmployeeNumber())
    print("Departments: ", manager.getManagedDepartment())
    print("Hire Date: ", manager.getHireDate())
    print("Salary: $", manager.getSalaryAmount())
    print("Raise: ", manager.getRaisePerc(), "%")
    manager.setRaise()
    print("Salary after raise: $", round(manager.getSalaryAmount(), 2))

    print("------------------------------------------------")

if __name__ == '__main__':
    main()
