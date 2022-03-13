#Camp Introduction
print("*****************************")
print("*** Sunshine Holiday Camp ***")
print("*****************************")
#Asking user for name, age, and choice of vegtable.
name = input("What is your name? ")
age = int(input("What is your age? "))
veg_list = ["Carrots", "Cucumber", "Radish", "Tomato", "Mixed Peas and Corn", "Butter Parsnip"]
assigned_veg = [0, 1, 2, 3, 4, 5]
if age <= 10 and age >= 7:
    #Items in veg_list are displayed to the user in terminal
    for veg, assigned_veg in zip(veg_list, assigned_veg):
        print("{}\t{}".format(veg, assigned_veg))
    vegnum = int(input("Please enter the vegtable you'd like to have, note that you should enter the number that is assigned to your vegtable: "))
    veggie = veg_list[vegnum]
    print("Hi", name, "welcome to Sunshine Holiday Camp.", "You are", age, "years old.")
    print("You have requested that you want", veggie + ".", "Great choice! Enjoy the camp!")
    #If user is between 11 and 12, inclusive of 11 and 12, they get to decide if they want a vegtable or not.
else:
    if age <= 12:
        veg_list = ["Carrots", "Cucumber", "Radish", "Tomato", "Mixed Peas and Corn", "Butter Parsnip", "None"]
        assigned_veg = [0, 1, 2, 3, 4, 5, 6]
        #Items in veg_list are displayed to the user in terminal
        for veg, assigned_veg in zip(veg_list, assigned_veg):
            print("{}\t{}".format(veg, assigned_veg))
        print("Please enter the vegtable you'd like to have.")
        print("Note that you should enter the number that is assigned to your vegtable: ")
        vegnum = int(input("If you do not want a vegtable enter 6: "))
        veggie = veg_list[vegnum]
        if veggie == veg_list[6]:
            print("Hi", name, "welcome to Sunshine Holiday Camp.", "You are", age, "years old.")
            print("You have requested you do not want any vegtables. Enjoy the camp!")
        else:
            print("Hi", name, "welcome to Sunshine Holiday Camp.", "You are", age, "years old.")
            print("You have requested that you want", veggie + ".", "Great choice! Enjoy the camp!")   
print("*****************************")
print("*** Sunshine Holiday Camp ***")
print("*****************************")