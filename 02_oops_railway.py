class RailwayForm:  #class Name
    def form(self):  #defining methods or variable
        print(f"Passenger name is {self.name}")  #printing statement using f string
        print(f"Train name is {self.train}")




applicationForm = RailwayForm()  #object instantiate
applicationForm.name = "sarthak singh"  #attribute 'sarthak singh' passed in variable name
applicationForm.train = "shiv ganga express"  
applicationForm.form()  #calling object associates  with methods/variable