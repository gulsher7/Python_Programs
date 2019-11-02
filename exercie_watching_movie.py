print(" ******************* HATE STORY 3: +18 ADULT ********************** ")

name,age = input(" enter your age and name \n Please put comma after one input \n Example:\n robin,21 \n ").split(",")
age = int(age)
name = name.title()
if name[0] == 'G' and age >= 14:
    print('you can watch movie')
else:
    print("sorry you can't watch movie")

print(name)
