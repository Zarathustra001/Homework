def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for item in numbers:
        if isinstance(item, (int, float)):
            result += item
        elif isinstance(item, str):
            print(f'Некорректный тип данных для подсчёта суммы - {item}')
            incorrect_data += 1
        else:
            try:
                result += float(item)
            except (TypeError, ValueError):
                print(f'Некорректный тип данных для подсчёта суммы - {item}')
                incorrect_data += 1
    return (result, incorrect_data)


def calculate_average(numbers):
    try:
        if not hasattr(numbers, '__iter__') or isinstance(numbers, str):
            if isinstance(numbers, str):
                numbers = list(numbers)  # Преобразуем строку в список символов
            else:
                raise TypeError('В numbers записан некорректный тип данных')

        sum_result, incorrect_count = personal_sum(numbers)
        if incorrect_count == len(numbers):
            return 0  # Если все элементы некорректны
        return sum_result / (len(numbers) - incorrect_count)
    except ZeroDivisionError:
        return 0
    except TypeError as e:
        print(e)
        return None


# Примеры вызовов функций
print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')