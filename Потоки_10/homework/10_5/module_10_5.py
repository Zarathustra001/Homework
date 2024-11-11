import time
import os
from multiprocessing import Pool, current_process


def read_info(name):
    """Считывает информацию из файла."""
    all_data = []  # Локальный список для каждого процесса
    try:
        with open(name, 'r', encoding='utf-8') as f: # явная обработка кодировки
            while True:
                line = f.readline()
                if not line:
                    break
                all_data.append(line)
    except FileNotFoundError:
        print(f"Файл {name} не найден.")
        return


if __name__ == '__main__':

    filenames = [f'./file {number}.txt' for number in range(1, 5)]


    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    end_time = time.time()
    print(f"Линейный вызов: {end_time - start_time}")



    # Многопроцессный вызов
    start_time = time.time()
    with Pool(processes=os.cpu_count()) as pool:  # Используем все доступные ядра
        pool.map(read_info, filenames)
    end_time = time.time()
    print(f"Многопроцессный вызов: {end_time - start_time}")