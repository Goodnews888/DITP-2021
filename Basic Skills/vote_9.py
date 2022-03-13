age = int(input("What is your age?: "))

if age >= 18: 
    print("As you are 18, you are allowed to vote")
    print('Pick your leader')
    leaders = 'Paul'
    print("Your choices are:\n", leaders)
    choice = input()
    if choice == leaders:
        print("Paul is now the dictator of this fake country")
    else:
        print("...ok")
elif age < 18: print("You are not old enough to vote")