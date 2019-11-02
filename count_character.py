name = input("enter your name")
i = 0
temp = ""
while i < len(name):
    if name[i] not in temp:
        temp += name[i]
        print(name[i], name.count(name[i]))
    i += 1
