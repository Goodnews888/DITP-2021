num = int(input("How many numbers to be averaged? "))
total_sum = 0

for n in range(num):
    numbers = float(input('Enter number: '))
    total_sum += numbers
print("Total is", total_sum)
avg = total_sum/num
print("Average of", num, "numbers is :", avg)
