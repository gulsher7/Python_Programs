import  time
t1 = time.time()
class Person:
    count = 0
    def __init__(self):
        Person.count += 1

obj1 = Person()
obj1 = Person()
obj1 = Person()
obj1 = Person()
obj1 = Person()
obj1 = Person()
print(Person.count)

t2 = time.time()
print(t2 - t1)