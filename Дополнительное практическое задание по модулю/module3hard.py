def sum(data_structure):
    total = 0
    if isinstance(data_structure, (list, tuple, set)):
        for item in data_structure:
            total += sum(item)
    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            total += sum(key)
            total += sum(value)
    elif isinstance(data_structure, str):
        total += len(data_structure)
    elif isinstance(data_structure, (int, float)):
        total += data_structure
    return total

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = sum(data_structure)
rows_count = len(data_structure)  # Вычисляем количество строк

print(f"Сумма всех чисел: {result}")
print(f"Количество строк: {rows_count}")