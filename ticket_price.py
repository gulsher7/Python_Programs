name = input("please enter your name")
age = int(input("enter your age "))

if age <= 3:
    print(f"hello {name} your ticket is free")
elif age >= 4 and  age <= 10:
    price = 150
    print(f" Hi {name } your ticket price is {price} ")
elif age >= 11 and age <=60:
    price = 250
    print(f"Hello {name } your ticket price is {price} ")
elif age >= 60:
    price = 200
    print(f"Hi {name } your ticket price is {price}")

