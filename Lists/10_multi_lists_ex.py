#Multi-dimensional lists
#Examples

#Example 1
students = [['Marama', 21], ['Cheyenne', 20], ['Dyani', 19]]
for student in students:
    name = student[0]
    age = student[1]
    print('{} is {}'.format(name, age))

#Example 2
for e in students:
    print(e)

#Example 3
for l in students:
    print(l[0])
    print(l[1])
