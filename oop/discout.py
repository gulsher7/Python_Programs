class Laptop:
    def __init__(self, name, model_no, price):
        self.laptop_name = name
        self.laptop_model_no = model_no
        self.laptop_price = price

    def discount(self,dis):
        self.dis = (self.laptop_price * dis)/100
        
    def full_detail(self):
        return f"{self.laptop_name} {self.laptop_model_no} {self.laptop_price} "



obj1 = Laptop('hp', 'i5', 58970)
print(obj1.full_detail())

print("original price is :", obj1.laptop_price)
obj1.discount(12)
print("after 12% discount")
print(obj1.dis)
