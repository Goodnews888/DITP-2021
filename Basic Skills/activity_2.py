#Program asks for user name, favourite color and two favourite colors
#Program is going to output a greeting and will do some Maths

#Created on: 28th July, 2021
#Created by: Connor Ghezzi

#Ask user for their name

name = input("What is your name? ")

#Ask user for their favourite color

favourite_color = input("What is your favourite color? ")

#Ask user for their favourite number

fav_num1 =int(input("What is your favourite number? "))
fav_num2 =int(input("What is your second favourite number? "))

#Do the maths
plus = fav_num1 + fav_num2
minus = fav_num1 - fav_num2
multiply = fav_num1 * fav_num2



#Output Greeting and print results
print("Hello", name)
print(favourite_color, "is your favourite color, which is the same as my favourite color")
print(fav_num1, "+", fav_num2, "=", plus)
print(fav_num1, "-", fav_num2, "=", minus)
print(fav_num1, "x", fav_num2, "=", multiply)



