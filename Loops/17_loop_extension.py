#Boxing Match

PlayerA_Score = 0
PlayerB_Score = 0
knockout = False
round = 0

while round < 10 and not knockout:
    round = round + 1
    print("Round " + str(round))
    PlayerA_round = int(input("Please enter your score for Player A: "))
    PlayerB_round = int(input("Please enter your score for Player B: "))
    PlayerA_Score += PlayerA_round
    PlayerB_Score += PlayerB_round

    if PlayerA_round == 0 or PlayerB_round == 0:
        knockout = True
print("Player A " , PlayerA_Score)
print("Player B " , PlayerB_Score)
print("Rounds fought: ", round)

if PlayerA_Score > PlayerB_Score:
    print("Player A is the winner. ")
elif PlayerB_Score > PlayerA_Score:
    print("Player B is the winner. ")
else:
    print("The match was a tie")


      
