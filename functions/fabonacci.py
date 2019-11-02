num = int(input("enter a number"))
def fabonacci(num):
        a = 0
        b = 1
        if num == 1:
            print(a)
        elif num == 2:
            print(a, b)
        else:
            print(a, b, end = " ")
            for x in range(num-2):
                c = a + b #1
                a = b # 1
                b = c # 1
                print(b, end = " ")
    
(fabonacci(num))
