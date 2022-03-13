#get 4 digit pin
#set the guess to 0.
#while guess is less than 4 digit pin - increment the guess.
#once loop stops, the guess number will be the pin.
#If the guess is a 1 digit - display it padded  with 3 0's
#If the guess is a 2 digit number - display with 2 0's
#If the guess is a 3 digit number - display with 1 0's

SECRET = int(input("Enter your secret 4 digit pin: "))
hack = 0

while hack < SECRET:
    hack = hack + 1
if hack < 10:
    print("Your secret is " + "000" + str(hack))
elif hack < 100:
    print("Your secret is " + "00" + str(hack))
elif hack < 1000:
    print("Your secret is " + "0" + str(hack))
else:
    print("Your secret is " + str(hack))


