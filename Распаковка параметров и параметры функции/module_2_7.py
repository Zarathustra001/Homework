#1.Функция с параметрами по умолчанию:
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()  # 1 'строка' True
print_params(10)  # 10 'строка' True
print_params(b=25)  # 1 25 True
print_params(c=[1, 2, 3])  # 1 'строка' [1, 2, 3]


#2. Распаковка параметров:


values_list = [10, 'Строка', False]
values_dict = {'a': 20, 'b': 'Другая строка', 'c': True}

print_params(*values_list)  # 10 'Строка' False
print_params(**values_dict)  # 20 'Другая строка' True

#3. Распаковка + отдельные параметры:


values_list_2 = [54.32, 'Еще строка']
print_params(*values_list_2, 42)  # 54.32 'Еще строка' 42
