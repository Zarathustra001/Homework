def get_matrix(n, m, value):
    if n <= 0 or m <= 0:
        return []  # возвращаем пустой список, если n или m меньше или равны 0

    matrix = []  # создаем пустой список для матрицы

    for i in range(n):
        row = []  # создаем пустую строку для текущей строки
        for j in range(m):
            row.append(value)  # добавляем значение value в текущую строку
        matrix.append(row)  # добавляем текущую строку в матрицу

    return matrix  # возвращаем готовую матрицу

# Получаем значения n, m и value от пользователя
n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))
value = int(input("Введите значение для заполнения матрицы: "))

# Получаем матрицу от функции get_matrix
matrix = get_matrix(n, m, value)

# Выводим результат построчно
for row in matrix:
    print(row)