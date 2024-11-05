import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100  # Всем по сотне, пусть попотеют, черти
        self.days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.enemies > 0:
            self.enemies -= self.power
            self.days += 1
            time.sleep(1)  # Задержка на денёк, пусть вражина понервничает
            print(f"{self.name} сражается {self.days}дней(дня), осталось {max(0, self.enemies)} воинов.") # max(0, self.enemies) -  чтобы не уйти в минус с врагами, а то как-то не трушно получается
        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


# Создаём наших бравых ребят
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Напускаем их на врагов, пусть мясо крошится!
first_knight.start()
second_knight.start()

# Ждём, пока эти красавчики закончат свою кровавую баню.
first_knight.join()
second_knight.join()


print("Битва окончена, парни! Всем наваляли!")