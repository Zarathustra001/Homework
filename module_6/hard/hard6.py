class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = color

        # Если количество переданных сторон не совпадает с sides_count, устанавливаем стороны по умолчанию
        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = list(sides)

        self.filled = False

    # Метод для получения цвета
    def get_color(self):
        return self.__color

    # Приватный метод для проверки корректности цвета
    def __is_valid_color(self, r, g, b):
        return all(isinstance(value, int) and 0 <= value <= 255 for value in (r, g, b))

    # Метод для установки цвета
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    # Приватный метод для проверки корректности сторон
    def __is_valid_sides(self, *new_sides):
        return (len(new_sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_sides))

    # Метод для получения сторон
    def get_sides(self):
        return self.__sides

    # Метод для установки новых сторон
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    # Перегрузка метода len() для вычисления периметра
    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.__calculate_radius()

    def __calculate_radius(self):
        # Расчет радиуса на основе длины окружности (единственной стороны)
        circumference = self.get_sides()[0]
        radius = circumference / (2 * 3.14)
        return radius

    def get_square(self):
        # Площадь круга: πr^2
        return 3.14 * (self.__radius ** 2)

    def set_sides(self, *new_sides):
        super().set_sides(*new_sides)
        self.__radius = self.__calculate_radius()


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1:
            sides = [sides[0]] * self.sides_count
        super().__init__(color, *sides)

    def get_volume(self):
        side_length = self.get_sides()[0]
        return side_length ** 3


# Пример использования:

circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

