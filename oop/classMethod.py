class Fruits:
    count = 0
    def __init__(self):
        Fruits.count += 1
    
    @classmethod
    def count_instance(cls):
        return f"you have created {cls.count} instance of {cls.__name__} "

obj1 = Fruits()
obj1 = Fruits()
print(Fruits.count_instance())

