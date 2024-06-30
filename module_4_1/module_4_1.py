from fake_math import divide as fake_divide
from true_math import divide as true_divide

while True:
    try:
        first = float(input("Введите первое число: "))
        second = float(input("Введите второе число: "))
        break
    except ValueError:
        print("Пожалуйста, введите корректные числовые значения.")

result_fake = fake_divide(first, second)
result_true = true_divide(first, second)

print(f"Результат деления {first} на {second} в fake_math: {result_fake}")
print(f"Результат деления {first} на {second} в true_math: {result_true}")