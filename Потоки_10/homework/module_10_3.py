import threading
import random
import time

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            self.balance += amount
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f"Пополнение: {amount}. Баланс: {self.balance}\n")
            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            print(f"Запрос на {amount}\n")
            if amount <= self.balance:
                self.balance -= amount
                print(f"Снятие: {amount}. Баланс: {self.balance}\n")
            else:
                print("Запрос отклонён, недостаточно средств\n")
                self.lock.acquire()
            time.sleep(0.001)



bk = Bank()

# Создаём потоки.  target -  наша функция, args - аргументы, которые ей передаём (в нашем случае это объект bk)
th1 = threading.Thread(target=bk.deposit, args=()) #  deposit не принимает аргументов, кроме self, который передаётся автоматически
th2 = threading.Thread(target=bk.take, args=())  #  take тоже самое

# Запускаем движуху!
th1.start()
th2.start()

# Ждём, пока потоки завершатся
th1.join()
th2.join()

print(f"Итоговый баланс: {bk.balance}")