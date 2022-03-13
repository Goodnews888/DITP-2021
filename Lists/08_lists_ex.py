#Lists in Python Exercises 2
#Exercise 4

#Obj: Ask the user for a list of names. Add each name to a list.
#Use at least five names.

#When the user is finished adding names, print them all out in a sentence.

names = []
min = 0
max = 0
while max < 5:
    max = int(input("Please enter at least 5 names you'd like to enter: "))
    if max < 5:
        print("You have entered less than 5 names, please try again. ")
    else:
        print("You wish to enter", max, "names, please name them. ")
while min < max:
    min += 1
    name = str(input("Please enter name " + str(min) + ": "))
    names.append(name)
for element in names:
        print(element)