class Calculator:

    def __init__(self,num):   #defining constructor
        self.number = num

    def square(self):   #function for square
        
        print(f"Square of the {self.number} is {self.number **2}")
        

    def cube(self):
        print(f"cube of the {self.number} is {self.number **3}")

    def squareRoot(self):
        print(f"SquareRoot of the {self.number} is {self.number **0.5}")


i = int(input("enter the number\n"))   #user input
a = Calculator(i)
a.square()
a.cube()
a.squareRoot()