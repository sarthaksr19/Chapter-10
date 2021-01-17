class Sample:
    # def __init__(ram, name):
    #     ram.name = name   #yes, We can use any parameter on the place of self. but it's quit confusing for others who see our code that what actully parameter passed.

    # def __init__(slf, name):
    #     slf.name = name   # same as first intialisation.

    def __init__(self, name):  #most efficient way to use self parameter.
        self.name = name



obj = Sample("Ram")

print(obj.name)