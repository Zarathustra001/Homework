import threading
import time
import random
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None  # Изначально стол свободен


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10)) # Симулирует время приема пищи


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()  # Очередь для ожидающих гостей
        self.tables = list(tables)  # Список объектов Table в кафе

    def guest_arrival(self, *guests):
        for guest in guests:
            free_table = next((table for table in self.tables if table.guest is None), None) # Найти свободный стол
            if free_table: # Проверяет наличие свободных столов и обрабатывает размещение гостя за столом, в противном случае помещает гостя в очередь.
                free_table.guest = guest
                guest.start() # Запускает поток гостя (симуляция приема пищи)
                print(f"{guest.name} сел(а) за стол номер {free_table.number}")
            else:
                self.queue.put(guest)  # Добавляет гостя в очередь, если нет свободных столов
                print(f"{guest.name} добавлен(а) в очередь")


    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest for table in self.tables): # Продолжает работу, пока очередь не пуста или какой-либо стол занят
            for table in self.tables:
                if table.guest and not table.guest.is_alive():  # Проверяет, есть ли гость за столом и закончил ли он есть
                    print(f"{table.guest.name} поел(а) и ушел(а)")
                    print(f"Стол номер {table.number} теперь свободен")
                    table.guest = None # Освобождает стол
                    if not self.queue.empty():  # Проверяет, есть ли гости в очереди
                        next_guest = self.queue.get()  # Берет следующего гостя из очереди (FIFO)
                        table.guest = next_guest #Назначает следующего гостя за освободившийся стол
                        next_guest.start()  # Запускает поток следующего гостя
                        print(f"{next_guest.name} вышел(ла) из очереди и сел(а) за стол номер {table.number}")

            time.sleep(1)  # Периодически проверяет наличие свободных столов



# Создаём столы
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создаём гостей
guests = [Guest(name) for name in guests_names]
# Заполняем кафе столами
cafe = Cafe(*tables)  #  Распаковываем список столов
# Приём гостей
cafe.guest_arrival(*guests) #  Распаковываем список гостей
# Обслуживание гостей
cafe.discuss_guests()