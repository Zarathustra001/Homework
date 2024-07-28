class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        if color.lower() in self.__COLOR_VARIANTS:
            self.__color = color.lower()
        else:
            print(f"Цвет {color} недопустим")
            self.__color = None

    def get_model(self):
        return f"\033[34mМодель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        if self.__color == 'blue':
            return f"Цвет: \033[34m{self.__color}\033[0m"  # Вывести синим цветом
        return f"Цвет: \033[32m{self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        if self.owner == 'Fedos':
            print(f"\033[34mВладелец: {self.owner}\033[0m")  # Вывести синим цветом, если владелец Fedos
        else:
            print(f"\033[34mВладелец: \033[32m{self.owner}\033[0m")

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color.lower()
        else:
            print(f"\033[31mНельзя сменить цвет на {new_color}\033[34m")

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()