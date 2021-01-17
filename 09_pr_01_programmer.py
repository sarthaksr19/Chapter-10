class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, address):
        self.name = name 
        self.salary = salary
        self.address = address

    def getDetails(self):
        print(f"Name of the programmer is {self.name}")
        print(f"Salary of the programmer is {self.salary}")
        print(f"Address of the programmer is {self.address}")

programmmer1 = Programmer("Divyesh", 150000, "Ghaziabad")
programmmer2 = Programmer("Aman", 150000, "Modinagar")
programmmer3 = Programmer("Pranjal", 150000, "Meerut")
programmmer4 = Programmer("sagar", 150000, "Delhi")

programmmer1.getDetails()
programmmer2.getDetails()

programmmer3.getDetails()

programmmer4.getDetails()






