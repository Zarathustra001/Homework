class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for floor in range(1, new_floor + 1):
                print(floor)


# Создаем объект класса House
my_house = House('ЖК Эльбрус', 30)

# Вызываем метод go_to с произвольным числом
my_house.go_to(17)

# Проверяем случай с несуществующим этажом
my_house.go_to(39)

# Проверяем случай с отрицательным этажом
my_house.go_to(-1)