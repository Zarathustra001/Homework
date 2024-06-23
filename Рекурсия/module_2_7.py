def get_multiplied_digits(number):

    # Преобразуем число в строку
    str_number = str(number)

    # Основной задачей будет отделение первой цифры в числе: создайте переменную first и запишите в неё первый символ
    # из str_number в числовом представлении(int).
    first = int(str_number[0])

    # Возвращайте значение first * get_multiplied_digits(int(str_number[1:])).
    # Таким образом вы умножите первую цифру числа на результат работы этой же функции с числом, но уже без первой цифры
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))

    # Если же длина str_number не больше 1, тогда вернуть оставшуюся цифру first.
    else:
        return first

# Ввод числа
number = int(input("Введите целое число: "))

# Вычисление произведения цифр
result = get_multiplied_digits(number)

# Вывод результата
print(f"Произведение цифр числа {number} равно {result}")