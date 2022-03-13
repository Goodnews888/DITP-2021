#get number for prime test
#Prime is true
#set test to 2

NUMBER = int(input("Enter your number: "))

isPrime = True
test = 2

while test < NUMBER:
    if NUMBER % test == 0:
        isPrime = False
    test = test + 1
if isPrime:
    print(str(NUMBER) + " is a prime number")
else:
    print(str(NUMBER) + " is not a prime number")

