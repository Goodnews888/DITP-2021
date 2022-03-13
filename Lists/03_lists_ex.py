teams = ["Liverpool", "Man City", "Man United", "Chelsea"]
standings = [1, 2, 3, 4]
#You can enumerate() and zip() functions together.


for index, (team, standing) in enumerate(zip(teams, standings)):
    print("Team {}: {} \t{}".format(index + 1, team, standing))