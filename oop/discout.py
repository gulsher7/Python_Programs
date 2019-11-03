class Laptop:
    def __init__(self, name, model_no, price):
        self.laptop_name = name
        self.laptop_model_no = model_no
        self.laptop_price = price

    def discount(self,dis):
        self.discount_price = (dis/100)*self.laptop_price
        self.discount_price = self.laptop_price - self.discount_price 

        
    def full_detail(self):
        return f"{self.laptop_name} {self.laptop_model_no} {self.laptop_price} "



obj1 = Laptop('hp', 'i5', 50000)
print(obj1.full_detail())

print("original price is :", obj1.laptop_price)
obj1.discount(10)
print("after 10% discount")
print(obj1.discount_price)
