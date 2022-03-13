#Create a list of numbers

numbers = [1, 2, 3, 4, 5, 5.5, 6.5, 7.5]
#Adding 60 to the end of the list in "numbers" variable
numbers.append(60)


#A list of names

names = ["Sarah", "Josie", "Andy"]
names.append("John")

#A list of mixed values

mixed = [3, "Pizza", "Peaches", 3.5]
mixed.append(3.14159)

print(numbers)
print(names)
print(mixed)
#Remember that Python uses zero-based indexing, so count starts at 0

#Finding the 2nd item in the numbers list
print(numbers[1])

#Finding the 4th item in the names list
print(names[3])