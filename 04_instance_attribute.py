class Employee:
    company = "Asus" # class attribute.
    salary = 400   #class attribute.

ram = Employee()
sarthak = Employee()

ram.salary = 500      # instance attribute
sarthak.salary =300

print(ram.salary)        ''' first it goes in objectand check whether there is instance attribute defined for salary in object or not.
 if doesn't then it goes to check the class attribute. if neither of two present in the program it throws the error.'''
print(sarthak.salary)

print(sarthak.company)
print(ram.company)