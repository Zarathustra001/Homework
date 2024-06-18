# Ввод числа от пользователя от 3 до 20
number = int(input("Введите число от 3 до 20: "))
while number < 3 or число > 20:
    number = int(input("Введите число от 3 до 20: "))

# Вторая вставка для пар чисел
Pass_for_number = ""

# Перебираем числа от 1 до 20
for i in range(1, 20):
    # Проверяем, делится ли первое число на сумму значений пары чисел
    for j in range(i + 1, 20):
        if number % (i + j) == 0:
            pass_for_number += str(i) + str(j)

print("Пароль для числа:", pass_for_number)