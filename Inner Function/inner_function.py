def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()  # Вызов inner_function внутри test_function


test_function()  # Вызов test_function (и, следовательно, inner_function)

# Попытка вызвать inner_function вне test_function
try:
    inner_function()
except NameError as a:
    print(f"Ошибка: {a}")
