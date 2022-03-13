#Get input frm user for the number to generate times table for
#input will give a string so we need to use int(input)...

times_table = int(input("Which times tables do you want?: "))
how_high = int(input("How high should I go?: "))

print()

#Generate times tables using a while loop
count = 1
while count <= how_high:
    answer = (count*times_table)
    print("{} X {} = {}".format(count, times_table, answer))
    count = count+1

