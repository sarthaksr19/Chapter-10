class Employee:
    company = "Asus"

ram = Employee()
sarthak = Employee()
# print(sarthak.company)
# print(ram.company)

Employee.company = "Dell"  #changing the class attribute via taking the class name fwolled with methods.

print(sarthak.company)
print(ram.company)
