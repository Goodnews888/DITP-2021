#While k is less than 20, print it. Set k to zero to start (initialise).
k = 0
while k < 20:
    print("k is less than 20, it is", k)
    k = k + 1
else:
    print("k is 20")
print()
print()
print()
print()
print()
print()
print()
#A cup of tea is the right temperature to drink at 112 degrees. If the temperature starts
#at 115, how can we write a while loop to tell a person when it is cool enough to drink?

cup = 115
print("The cup is 115*C so it is too hot to drink")
while cup >= 112:
    print(cup)
    cup = cup - 1
print("The cup is now cool enough to drink")

print()
print()
print()
print()
print()
print()
print()


#You are to write a program for someone who wants to save to go on a trip to Fiji. 
#They need $2000. They work part time at McDonals and so you want them to save some of their pay,
#after their expenses - which you will find from them. You will have to work out how long
#it will take them to save $2000. They currently have $10 in their bank account.

#Let their hourly wage be $20 and daily expenses be $-8

target = 2000
bankBalance = 10
numWeeks = 0

income = float(input("What is your weekly income? "))
expenses = float(input("What are your weekly expenses? "))

while bankBalance < target:
    savings = income - expenses
    numWeeks = numWeeks + 1
    bankBalance = bankBalance + savings

print ("You will reach your goal of saving $2000 in", numWeeks, "weeks.")
print("It will take", numWeeks, "weeks to save for your trip to Fiji.")

input("\n\nPress the enter key to exit.")

