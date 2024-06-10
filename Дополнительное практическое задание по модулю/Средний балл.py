grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Преобразуем множество students в упорядоченный список
students_list = sorted(students)

# Создаем пустой словарь для хранения средних баллов
average_grades = {}

# Перебираем в цикле имена учеников
for student in students_list:
    # Получаем список оценок для ученика по его имени
    student_grades = grades[students_list.index(student)]

    # Считаем сумму оценок ученика
    total_grade = sum(student_grades)

    # Считаем количество оценок ученика
    num_grades = len(student_grades)

    # Вычисляем средний балл ученика
    average = total_grade / num_grades

    # Добавляем имя ученика и его средний балл в словарь
    average_grades[student] = average

# Выводим результат в консоль
print(average_grades)