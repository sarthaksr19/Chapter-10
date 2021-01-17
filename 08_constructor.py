class Employee:
    Company = "NiKon"
    def __init__(self, name, salary, subunit):
        self.name = name 
        self.salary = salary
        self.subunit = subunit
        print("Employee is created")  #__init__ function printed this statement.
    
    def getDetails(self):
        print(f"The name of the employee is {self.name} and his basic salary is {self.salary} working in the {self.subunit} subunit.")

sarthak = Employee("Sarthak", 150, "Camera")
sarthak.getDetails()
