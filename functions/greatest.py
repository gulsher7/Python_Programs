num1,num2,num3 = 2,3,6

def greatest(x,y,z):
    if x > y and x > z:
        print(f"{x} is greater than {y} and {z}")

    elif y > x and y > z:
        print(f"{y} is greater than {x} and {z}")
    else: 
        print(f"{z} is greater than {x} and {y}")


result = greatest(num1,num2,num3)