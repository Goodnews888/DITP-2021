#Lists in Python Exercises 2
#Exercise 5

#Obj: Shopping list - ask the user for a bunch of products to buy at the supermarket.
#When they've finished, print out a nicely formatted shopping list.

items = []
min = 0
max = 0
while max < 1:
    max = int(input("Please enter number of items you'd like to purchase: "))
    if max < 1:
        print("You have entered no items, please try again: ")
    else:
        print("You wish to enter", max, " items, please name them. ")
while min < max:
    min += 1
    item = str(input("Please enter item " + str(min) + ": "))
    items.append(item)
print("Shopping List: ")
for element in items:
        print(element)
    


