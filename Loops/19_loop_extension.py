#Problem 6
#19/09/2021

#5 Races in a sporting event - use a for loop to collect and display
#the winner's names for each event.
mylist = []
round = 0
while round < 5:
    round+=1
    ele = str(input("Please enter the winner of race " + str(round) + ": "))
    print(ele)
    
    mylist.append(ele)

print(mylist)