class Phone:
    def __init__(self, phone_name, phone_model, phone_price):
        self.phone_name = phone_name
        self.phone_model = phone_model
        self.phone_price = phone_price
    
    def full_name(self):
        self.result = self.phone_name  + " "+  self.phone_model
        return f"{self.result}"
    
class Smartphone(Phone):
    def __init__(self, phone_name, phone_model, phone_price, ram, internal_memory):
        super().__init__(phone_name, phone_model, phone_price)
        self.ram = ram
        self.internal_memory = internal_memory

class FlagSale(Smartphone):
    def __init__(self, phone_name, phone_model, phone_price, ram, internal_memory, camera):
        super().__init__(phone_name, phone_model, phone_price, ram, internal_memory)
        self.camera = camera

obj1 = Phone('Redmi', 'Note 7 Pro', 14500)
print(obj1.full_name())
obj2 = Smartphone('Nokia', '2630', 7854, '4GB', '64GB')
print(obj2.full_name())
obj3 = FlagSale('Nokia', '2630', 7854, '4GB', '64GB', '105Mpx')
print(obj3.camera)


    
