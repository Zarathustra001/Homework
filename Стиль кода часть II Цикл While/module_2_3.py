my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
#Чтобы перебрать список вам понадобиться обращение по индексу, запишите в отдельную переменную начальное значение - 0.
index = 0
#Чтобы не выйти за границу списка, в условии цикла while рекомендуется сравнивать текущий индекс и длину списка
while index < len(my_list):
    number = my_list[index]

    if number <= 0:
        break

    print(number)

    index += 1