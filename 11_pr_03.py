class Bank:
    bankName = "State Bank of india"
    a = 1500          # class attribute

obj = Bank()
obj.a = 0    #instance attribute
print(Bank.a)
print(obj.a)


'''question is does this change the class attribute

answer:- no, it can't change beacuse we define object instance as obj.a = 0  and class attribute 

is 1500 as hence we know both are different no matter sharing same names.'''


