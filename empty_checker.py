name = input("etner your name ")

if name.isspace():
     print("you enter a space")

elif name:
     print(f"your name is { name.title() }")

else:
    print("you didn't type anything")

