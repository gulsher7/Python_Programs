num1 = int(input("enter first number"))
num2 = int(input("enter second number"))

def checkerNum(x,y):
     return  "num1 is greater"  if num1 > num2 else " num2 is greater" #Ternary Operators


result = checkerNum(num1,num2)
print(result)
