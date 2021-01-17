class Train:

    def __init__(self,name, seats, fare):  #intialisation
        self.name = name
        self.seats = seats
        self.fare = fare

    def getStatus(self):    #defining function.
        print(f"Name of the train is {self.name}")
        print(f"Seat availibility of this train is {self.seats}")


    def getFare(self):   #defining function.
        print(f"Fare of the journey is Rs {self.fare}")

    def bookTicket(self):     #defining function.
        if self.seats > 0:     #condtion to check whether seats are available or not.
            print(f"CONGRALUTIONS! Your ticket is Booked. Your seat number is {self.seats}. We wish you a Safe Journey.")
            self.seats = self.seats - 1
        else:
            print("Sorry for your inconvinence but No seats are available!")

    def cancelTicket(self):   #defining function.
        print(f"your ticket is cancelled!!!")
        self.seats = self.seats + 1
        


indianRailway = Train("Shiv Ganga Express : 12560", 2, 450)  # object instanciate.

## calling the functions.

indianRailway.getStatus()
indianRailway.getFare()
indianRailway.bookTicket()
indianRailway.getStatus()
indianRailway.cancelTicket()
indianRailway.getStatus()



