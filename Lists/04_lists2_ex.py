numbers = [3, 5, 7, 13, 21, 4, 25, 29, 7, 15]
guesses = []
guessed = False
while not guessed:
    guess = int(input("Your guess of the integer: "))
    if guess in numbers:
        print("yes, {} is in the set.".format(guess))
        guessed = True
    else:
        print("Sorry that number is not in the set. Please try again.")
        guesses.append(guess)
        print("You have guessed {}".format(guesses))