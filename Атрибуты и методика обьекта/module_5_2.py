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

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"


# Создаем объект класса House
my_house = House('ЖК Эльбрус', 10)
my_house2 = House('ЖК Акация', 20)

# Выводим информацию о здании
print(my_house)
print(my_house2)

# Должен возвращать кол-во этажей здания self.number_of_floors
print(len(my_house))
print(len(my_house2))