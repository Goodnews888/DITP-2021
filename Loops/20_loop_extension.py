"""A golf game has 9 or 18 holes. Ask the user which length of game i being played,
and write a loop which collects the score for each hole and tallies them."""

'''holes = int(input("Please enter if the golf game either has 9 or 18 holes: "))
total = 0
hole = 1
while hole <= holes:
    score = int(input("Enter score for hole " + str(hole) + ": "))
    hole+=1
    total = score + total
print("Your total score is", total)'''


#List of Computer Manufactureres

#Create list of Manufactureers
ManufactureList = ["HP","DELL","Acer","Asus","Toshiba"]

#Set up variables
totalnum = 4
count = 0

no_items = 0
for element in ManufactureList:
    no_items += 1
print("Number of elements in the list: ", no_items )

#Start to loop
while count < no_items :
    print(ManufactureList[count])
    count = count + 1
