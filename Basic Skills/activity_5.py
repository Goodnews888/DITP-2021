

#Setting the minimum age to 14
minage = 14

#Printing introduction to the babysitting club to the user
print("Welcome to the Babysitting Club")
print("We are looking for new babysitters!")
print("You must be at least",minage," to be a babysitter")
print()


name = input("What is your name?: ")
age = int(input("How old are you?: "))
#Checking if user is at least 14 years of age.
if age < minage :print("Sorry", name ,',', age, "is too young to be a babysitter.".format(name))
if age >= minage :print(name, age,"is a great age to be a babysitter.")

#Testing out if statements
#number = 5
#if number < 5 : print("less than 5")
#if number == 5 : print("equal to 5")
#if number > 5 : print("greater than 5")
#if number != 5 : print("not equal to 5")

