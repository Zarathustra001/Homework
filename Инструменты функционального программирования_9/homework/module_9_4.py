from random import choice

# Lambda-функция
first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))
print(f"Lambda-function result: {result}")



# Замыкание
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as f:  # Открываем файл в режиме добавления ('a')
            for data in data_set:
                f.write(repr(data) + '\n') # Записываем строковое представление data + перевод строки

    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])



# Метод call
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):  # Магический метод __call__ позволяет вызывать объект как функцию
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(f"MysticBall result 1: {first_ball()}")
print(f"MysticBall result 2: {first_ball()}")
print(f"MysticBall result 3: {first_ball()}")