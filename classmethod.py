class Employee:
    def __init__(self, fname,lname,salary):
        self.f = fname
        self.l = lname
        self.s = salary
     
    def increment(self):
        self.s = int(self.s * Employee.increase)

    @classmethod
    def changeincrement(cls, amount):
        cls.increase = amount

rahul = Employee('rahul', 'sharma', 20)

print(rahul.s)
Employee.changeincrement(2)
rahul.increment()
print(rahul.s)


