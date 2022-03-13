#Write a Python function that takes a list and returns a new list with unique elements of the first list.
'''def unique_list(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x
print(unique_list([1,2,3,3,3,3,4,5]))'''

#Write a Python function that takes a number as a parameter and check the number is prime or not.
#Note: A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors
#other than 1 and itself.
'''def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2, n):
            if(n % x==0):
                return False
        return True
print(test_prime(27))'''

#Write a Python program to print the even numbers from a given list.
# Sample List: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result: [2, 4, 6, 8]

'''def is_even_num(l):
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum
print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))'''



