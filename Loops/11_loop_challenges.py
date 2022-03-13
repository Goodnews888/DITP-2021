#Pg 26 Problem 6
#Calculate a sum of numbers between 1 and 5
list = range(1, 5)
sum1 = sum(list)
print(sum1)

#Pg 26 Problem 7
sum2 = 1
for i in range(10,20):
    sum2 *= i     #sum = sum * i
print(sum2)

#Pg 26 Problem 8
count = int(input("How many numbers would you like to add? "))
num = 0
sum4 = 0
while num < count:
    sum3 = int(input("Enter a number: "))
    sum4 += sum3
    num = num + 1
print(sum4)




    