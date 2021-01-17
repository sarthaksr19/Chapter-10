class Employee:
    Company = "Asus"
    def getSalary(self):   #self is a parameter which passes automatically and also it offers to use instance attribute and class attribute. 
        print(f"salary for this employee is {self.salary} in {self.Company}")

ram = Employee()
ram.salary = 150000
ram.getSalary()   # or in another word it is like Employee.getSalary(ram) so we pass one argument in getSalary() function i.e, ram. 
# that's why we use self keyword in a define function.