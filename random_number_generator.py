import random
guess_number = int(input("enter a guess number "))

numbers = []
for x in range(2,11,2):
    numbers.append(x)
winning_number = random.choice(numbers)

if winning_number == guess_number:
    print("Congratulations YOU WIN!!!!!")

elif guess_number > winning_number:
    print("your number is to high")

elif guess_number < winning_number:
    print("your no is low") 

print(numbers)