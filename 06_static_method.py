class Employee:
    Company = "Google"

    def getSalary(self):
        print(f"salary of this employee is {self.salary} in {self.Company}\n{self.signature}")

    @staticmethod   #so here as we see below with greet function we don't pass self parameter as we see in the code.
    def greet():  #if we don't wanna pass self parameter in greet function then we use here static method.
        print("Good Morning! Sir")

ram = Employee()
ram.signature = "Thanks!"

ram.salary = 150000
ram.greet()
ram.getSalary()
