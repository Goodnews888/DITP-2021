INTEREST_RATE = float(input("What is the interest rate? "))
YEARS = int(input("Enter the investment period (years): "))

principal = 1000

yearCount = 0

while yearCount < YEARS:
    interest = principal * INTEREST_RATE/100
    principal = principal + interest
    yearCount = yearCount + 1
print("AFter " + str(yearCount) + " years, your balance is $" + "{0:.2f}".format(principal))