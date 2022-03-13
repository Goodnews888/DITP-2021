"""age = int(input("Please enter your age: "))
if age <= 10:
    race_length = 100
else:
    race_length = 200
print("The race you'll be running is", race_length, "meters")"""

min_age = int(input("Please enter your age: "))
if min_age >=16:
    print("You are old enough to donate blood: ")
    min_weight = float(input("Please enter your weight: "))
    if min_weight >= 50:
        print("You meet the weight requirements to donate blood: ")
    else:
        print("You have to be atleast 50kgs to donate blood.")
else:
    print("You have to be atleast 16 to donate blood: ")



"""Another way to do this is:
age = float(input("What is your age?: "))
weight = float(input("What is your weight in kgs?: "))

DONOR_AGE_LIMIT_LOW = 16
DONOR_AGE_LIMIT_HIGH = 70
DONOR_WEIGHT_LIMIT = 50

if age >= DONOR_AGE_LIMIT_LOW and age <= DONOR_AGE_HIGH and weight >= DONOR_WEIGHT_LIMIT
    print("Eligible to donate blood.") 
else:
    print("Not eligible to donate blood.")
    """

