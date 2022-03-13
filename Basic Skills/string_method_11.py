statement = "           tHe dOg barkS at midnIght "
print(statement.upper())
print()
print(statement.lower())
print()
print(statement.title())
print()
print(statement.swapcase())
print()
print(statement.split())
print()
print(statement.replace("",'"'))
print(statement.strip())
print()
print(statement.replace("dOg","barkS"))

"""statement.lower()
statement.lower()
statement.swapcase()
statement.split()
statement.strip()
statement.replace("","")
statement.replace("DOG","CAT").replace("barks","hisses").replace("MIDNIGHT","DAWN")"""


sister_age = int(input("Please input the sister's age: "))
brother_age = int(input("Please input the brother's age: "))

if sister_age > brother_age: print("The sister is older than the brother.")
if sister_age < brother_age: print("The brother is older than the siter.")
if sister_age == brother_age: print("The brother and the sister are the same age")

