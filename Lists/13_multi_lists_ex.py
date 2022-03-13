#Multi-dimensional lists 
#Exercise 5 Extension (Not in Google Classroom)

orders = []

ordering = True
while ordering:
    flavour = input("Enter the pizza flavour you would like, or 'quit' to complete your order: ")
    if flavour.lower()=="quit":
        ordering = False
    else:
        quantity = int(input("How many {} would you like? ".format(flavour)))
        order = [flavour, quantity]
        orders.append(order)


#Receipt
print("\nYour order:")
total = 0
for order in orders:
    flav = order[0]
    quan = order[1]
    total += quan
    print("- {} {}".format(quan, flav))

print("Total: {} ingredients.".format(total))


