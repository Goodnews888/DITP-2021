#Prize game (Note not releated to functions ^)
#Welcome to the prize game
#Set up the list of prizes
prizelist = ["holiday to Vegas", "Microsoft Surface", "chicken dinner", "iPhone", "box of pens"]

#ask for envelope number
prizenum = int(input("Pick an envelope between 1 and 5 to choose your prize: "))
#work out what prize they have won
prize = prizelist[prizenum-1]
print("")
print("WINNER WINNER WINNER WINNER WINNER WINNER")
print("WINNER WINNER WINNER WINNER WINNER WINNER")
print("")
print("Congratulations, you have won the", prize)
print("")
print("WINNER WINNER WINNER WINNER WINNER WINNER")
print("WINNER WINNER WINNER WINNER WINNER WINNER")
print("")