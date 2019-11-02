class Laptop:
    def __init__(self, name, model_no, price):
        self.laptop_name = name
        self.laptop_model_no = model_no
        self.laptop_price = price
        
    def full_detail(self):
        return f" {self.laptop_name} {self.laptop_model_no} {self.laptop_price} "

obj1 = Laptop('hp', 'i5', 45000)
print(obj1.full_detail())