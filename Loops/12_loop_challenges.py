#pg 27 Problem 9

num1 = float(input("Please enter the first number: "))
num2 = float(input("Please enter the second number: "))
print(round(num1 * num2, 2))
print(round(num1 + num2, 2))


#pg 27 Problem 10
num = 1
sum1 = 0
count = 0
while num != 0:
    sum = int(input("Please enter in a number: "))
    sum1 += sum
    count = count + 1
    yn = int(input("Would you like to enter in another number to add? If no enter 0, if yes enter 1: "))
    if yn == 1: num = num
    else: num = num - 1
print("The average of these numbers are", sum1/count)
