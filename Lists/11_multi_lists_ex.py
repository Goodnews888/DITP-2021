#Multi-dimensional lists
#Exercise 1 

shopping = [["Bread", 2], ["Milk", 3], ["Cheese", 1], ["Nappies", 5]]

print("Shopping List: ")

for item in shopping:
    name = item[0]
    cost = item[1]
    print('{} costs ${}'.format(name, cost))
print()

#Exercise 2

results = [["Maths", 75], ["English", 62], ["PE", 45], ["DT", 100]]

print("####  RESULTS  ####")
print()

for result in results:
    subject_name = result[0]
    percentage = result[1]

    if percentage >= 90:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "F"
    print("{}: {} {}%".format(subject_name, grade, percentage))
print()

#Exercise 3

#Given the list
courses = [["DT", 58, "Brook"], ["English", 122, "Brook"], ["Science", 95, "Tower"], ["History", 156, "Pipitea"]]
#Print out a list of courses, which building they're in, and how many students they have.

for course in courses:
    subject = course[0]
    no_students = course[1]
    building = course[2]
    print("{}: {} students in building {}".format(subject, no_students, building))


