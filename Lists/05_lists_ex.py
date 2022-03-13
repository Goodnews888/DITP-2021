#Lists in Python Exercise 2
#Connor G 26/10/2021

#Exercise 1
#Write a program that asks the user for what 5 toppings they want on their pizza.
number = 0
toppings_list = []
max = int(input("How many toppings would you like?: "))
print("Welcome to Pesto's Pizza, what 5 toppings would you like with your pizza?")
while number < max:
    number+= 1
    toppings = str(input("Please enter topping " + str(number) + ": "))
    toppings_list.append(toppings)

print("Thank you for ordering with Pesto's Pizza, here is a review of what pizza you ordered.")
print()
for ele in toppings_list:
    print("{}\t".format(ele))




