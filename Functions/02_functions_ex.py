#Exercise 1
#Write a function that aks for two numbers and prints the toal of the two.
#Call the function twice in your main code.
'''def function1(x, y):
    return x + y
a = function1(int(input("Enter a number: ")), int(input("Enter another number: ")))
print(a)'''
#Exercise 2
#Write a function that that calculates the area of a rectangle after asking for it's height and width.
'''def function2(x, y):
    return x * y
b = function2(int(input("Enter the height of the rectangle: ")), int(input("Enter the width of the rectangle: ")))
print("The area of the rectangle is", b)'''
#More exercises on "functions"
#Write a Python function to find the Max of three numbers.

'''def maximum(a, b, c):
    list = [a, b, c]
    return max(list)
x = int(input("Enter First number: "))
y = int(input("Enter Second number: "))
z = int(input("Enter Third number: "))
print("Maximum Number is ::>", maximum(x, y, z))'''

#Write a Python function to sum all the numbers in a list. (Sample list: [8, 2, 3, 0, 7])
'''def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((8, 2, 3, 0, 7)))'''

#Write a Python function to multiply all the numbers in a list. (Sample List: [8,2,3,-1,7])
'''def sum(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total
print(sum((8, 2, 3, -1, 7)))'''

#Write a Python program to reverse a string. "1234abcd"
'''def string_reverse(x):
    return x[:: - 1]
mytxt = string_reverse("1234abcd")'''

#Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts
#the number as an arguement. 
'''def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n = int(input("Input a number to compute the factorial: "))
print(factorial(n))'''


#Write a Python function to check whether a number falls in a given range.
'''def test_range(n):
    if n in range(3,9):
        print( " %s is in the range"%str(n))
    else:
        print("The number is outside the given range.")
test_range(3)'''


#Write a Python function that accepts a string and calculates the number of uppercase letters and lowercase letters.
def string_test(s):
    d = {"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
            d["UPPER_CASE"]+=1
        elif c.islower():
            d["LOWER_CASE"]+=1
        else:
            pass
    print ("Original String: ", s)
    print ("No. of Uppercase characters: ", d["UPPER_CASE"])
    print ("No. of Lower case characters: ", d["LOWER_CASE"])
string_test('The quick Brown Fox')