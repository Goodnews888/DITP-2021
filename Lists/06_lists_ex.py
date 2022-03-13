#Lists in Python Exercises 2
#Exercise 2
#Pizza_orderer.py

print("Welcome to Pesto's Pizza")

orderer_name = input("What's your name? ")
pizza_amount = int(input("Thanks, {}. how many pizzas would you like? ".format(orderer_name)))

order = []
count = 0

while count < pizza_amount:
    flavour = input("Enter pizza flavour {}: ".format(count+1))
    order.append(flavour)
    count += 1

print("Thanks for your order!")
for pizza_flavour in order:
    print("- {}".format(pizza_flavour))
print("Enjoy!")