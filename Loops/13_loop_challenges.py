#Pg 30 
#Write a loop statement that will count from 1 to 12 inclusive.
#Insde the loop, write a pritn statement that uses i to print the 7 times table.
#You should print each line as "7 x 1 = 7" and so on using the .format().
for i in range(1, 13):
    print("{} * {} = {}".format(i, 7, i * 7))