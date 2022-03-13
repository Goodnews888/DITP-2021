#Multi-dimensional lists
#Exercise 4 - Appending 2 Dimensional Arrays

orders = []

while True:
    flavour = input("Enter the pizza flavour you would like, or 'quit' to complete your order: ")

    #Asking user to input flavour, if user inputs 'quit' program will break. 
    if flavour.lower()=="quit":
        break
    quantity = int(input("How many {} would you like? ".format(flavour)))
    order = [flavour, quantity]
    orders.append(order)

print(orders)
