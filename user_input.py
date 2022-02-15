#collecting user input

name = input("whats your name? ")
age = int(input("whats your age? "))
height = float(input("whats your height? "))


print("\nyour name is "+ name)
print("Your are "+ str(age)+"years old")
print("you are "+str(height)+"ft tall")

birthday = age + 1
x = input("Is it your birthday today?!!!")
if x == "Yes":
    print("happy birthday!!!")
    print("you are now "+ str(birthday)+"years old")
    print("your gift is on the way!!! HURRAY!!!")
else:
    print("im sorry u get nothing!!!")

