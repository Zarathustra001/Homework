grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_sort = sorted(students)

grades_m = []

for i in grades:
    a = sum(i)/len(i)
    grades_m.append(a)

b = dict()

for i in range(5):
    key = students_sort[i]
    value = grades_m[i]
    b[key] = value
print(b)