#Lists in Python Exercises 2
#Exercise 3

#29/10/21
#Connor

#Obj: Create a list with 10 integers between 1 and 30 (inclusive). 
#Ask the user to guess one of the numbers, end the program
#when one of the numbers is guessed.

#Extension:
#Keep track of numbers guessed and tell the user if they have 
#guessed the number before.

number_list = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
guesses = []
guessed = False

print("Hello user, here is a guessing game!")
print("Your objective is to guess one of the 10 numbers I chose between the range of 1 and 30 inclusive. ")
print("Good luck")
while not guessed:
    guess = int(input("Your guess of the integer: "))
    if guess in number_list:
        print("yes, {} is in the set.".format(guess))
        guessed = True
    else:
        print("Sorry that number is not in the set. Please try again.")
        guesses.append(guess)
        print("You have guessed {}".format(guesses))
