#Joining two lists

list1= ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#An alternate way is by appending all the items
#from 'list2' into 'list1'

for x in list2:
    list1.append(x)
print(list1)

#Or extend () method, which is to add elements from one list to another list:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

#Lists - iterating through a list
teams = ["Liverpool", "Man City", "Man United", "Chelsea"]
for x in teams:
    print(x)

#enumerate() is a built in function which is commonly used with lists. 
#It takes the list and returns it as an enumerate object - a list of tuples
#containing the value and its index. Remember the default starts at 0.
for x, team in enumerate(teams):
    print(x, team)

#zip() is a built in function which can be used to loop through multiple lists at once.
#It takes two or more equal-length lists and merges them together.
#Note: if the lists are not of equal length it will drop the items in the longest list.
print("Teams with their standing in the league")
standings = [1, 2, 3, 4]
for team, standings in zip(teams, standings):
    print("{}\t{}".format(team, standings))

