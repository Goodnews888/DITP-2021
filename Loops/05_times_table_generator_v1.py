#Asking user to input two numbers to generate a times table to however high they wish"
num1 = int(input("Please enter a number: "))
num2 = int(input("How high should I go?: "))

#Displaying all the possible times tables for the numbers the user has selected"
#Adding 1 to num2 because 
for i in range(1, num2 + 1):
    print("{} * {} = {}".format(i, num1, num1*i))
    