#Loops - while and for presentation pg 25 Problem 4.
target = 100
x = 3
y = 5
numTimes = 0
while x + y < target:
    x = x + 2
    y = y * 2
    numTimes = numTimes + 1
print("It will take", numTimes, "loops", "for x + y to be greater than 100")
print(x+y)

#Page 25 Problem 5
target = 2000000
numWeeks = 0
bankBalance = 0

income = float(input("What is your weekly income after tax? "))
expenses = float(input("What is your weekly expenses? "))
while bankBalance < target:
    savings = income - expenses
    numWeeks = numWeeks + 1
    bankBalance = bankBalance + savings
print("It will take", numWeeks, "weeks for you to reach your target of $2million dollars.")
print("Therefore it will take", numWeeks, "weeks for you to retire")


